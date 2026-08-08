import chainlit as cl
import os
from dotenv import load_dotenv
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# New imports for the data layer
import chainlit.data as cl_data
from custom_layer import CustomSQLAlchemyDataLayer
from typing import Optional
from chainlit.chat_context import chat_context
from chainlit.types import ThreadDict

from langchain_chroma.vectorstores import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings


# Load environment variables
load_dotenv()

# Set up the Anthropic model and prompt template
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    max_tokens_to_sample=4096,
    temperature=0.7,
    )

PROMPT_TEMPLATE = ChatPromptTemplate(
    [
        ("system", "You are a helpful ai assistant."),
        ("user", """
         <message history>
         {message_history}
         </message history>

         <context>
         {context}
         </context>
         
         User's question: {question}
         
         """),
    ]
)
PARSER = StrOutputParser()

# Set up the data layer
cl_data._data_layer = CustomSQLAlchemyDataLayer(
    conninfo="postgresql+asyncpg://myuser:mypassword@localhost:5432/mydatabase"
)

@cl.password_auth_callback
def auth_callback(username: str, password: str) -> Optional[cl.User]:
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin",
            metadata={"role": "admin", "provider": "credentials"},
            id="admin_id"
        )
    elif (username, password) == ("volkan", "volkan"):
        return cl.User(
            identifier="volkan",
            metadata={"role": "admin", "provider": "credentials"},
            id="volkan_id"
        )
    else:
        return None


@cl.on_chat_start
async def start():
    user = cl.user_session.get("user")
    if not user:
        await cl.Message(content="Please log in to start a chat.").send()
        return

    await cl.Message(content="Hello, I'm Claude! How can I help you today?", author="Assistant").send()



@cl.step
async def translate_to_english(message: cl.Message):
    prompt_template = ChatPromptTemplate(
        [
            ("system", "You are a translater assistant to translate sentences from Turkish to English."),
            ("user", "User's sentences: {question}"),
        ]
    )

    turkish_model = ChatOllama(
        model="gemma2:27b",
        num_predict=4096,
        base_url="http://localhost:11434",
        )

    # Create a chain with the prompt template and the model
    chain = prompt_template | turkish_model | PARSER
    # Invoke the chain with the user's question
    response = await chain.ainvoke(
        {
            "question": message.content,
        }
    )

    return response

@cl.step
async def search_vector(message: cl.Message):
    embedding_model = OllamaEmbeddings(
        model="bge-m3",
        base_url="http://localhost:11434",
    )
    vector_store = Chroma(persist_directory='db', embedding_function=embedding_model)

    # Search for similar documents
    docs = vector_store.similarity_search(message.content, k=5)
    return [doc.page_content.strip() for doc in docs]



@cl.on_message
async def main(message: cl.Message):
    user = cl.user_session.get("user")
    if not user:
        await cl.Message(content="User information not found. Please try logging in again.").send()
        return

    chain = PROMPT_TEMPLATE | MODEL | PARSER

    message_history = "\n".join([f"{m.author}: {m.content}" for m in chat_context.get()])
    translated_message = await translate_to_english(message)
    docs = await search_vector(message)

    response = await chain.ainvoke(
        {
            "question": translated_message,
            "message_history": message_history,
            "context": "\n".join(docs),
        }
    )

    await cl.Message(content=response, author="Assistant").send()


@cl.on_chat_resume
async def resume(thread: ThreadDict):
    pass