# 🚀 Building AI Applications with LangChain & LLMs

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-v0.3-green.svg)](https://python.langchain.com/)
[![Chainlit](https://img.shields.io/badge/UI-Chainlit-FF4B4B.svg)](https://chainlit.io/)
[![Ollama](https://img.shields.io/badge/Local_LLM-Ollama-black.svg)](https://ollama.ai/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Bu depo; **LangChain v0.3 (LCEL)**, **Chainlit**, **RAG**, **Neo4j**, **ChromaDB**, **Ollama** ve **Docker** kullanarak modern LLM uygulamaları geliştirmeye yönelik uçtan uca örnekler içerir.

---

## 📌 İçindekiler

- [Mimari Genel Bakış](#-mimari-genel-bakış)
- [Temel Özellikler ve Modüller](#-temel-özellikler-ve-modüller)
- [Teknoloji Yığını](#-teknoloji-yığını)
- [Proje Dizini](#-proje-dizini)
- [Kurulum ve Hızlı Başlangıç](#-kurulum-ve-hızlı-başlangıç)
- [Yazar ve İletişim](#-yazar-ve-iletişim)
- [Lisans](#-lisans)

---

## 📐 Mimari Genel Bakış

Proje, LLM tabanlı uygulamaları prototip aşamasından çalışır uygulamalara taşımak için aşağıdaki katmanları kullanır:

```text
+-----------------------------------------------------------------------+
|                    1. ARAYÜZ VE ORKESTRASYON                         |
|          Chainlit UI  |  Flowwise AI  |  REST API                    |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|                    2. LANGCHAIN & LCEL CORE                          |
|       Declarative Chains (|)  |  ReAct Agents  |  Custom Tools       |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|                    3. BİLGİ VE HAFIZA KATMANI                        |
|      ChromaDB (RAG)  |  Neo4j (Graph Memory)  |  PostgreSQL          |
+-----------------------------------------------------------------------+
                                    |
                                    v
+-----------------------------------------------------------------------+
|                    4. MODEL VE INFERENCE                             |
|       Ollama  |  Groq  |  Claude  |  GPT                             |
+-----------------------------------------------------------------------+
```

---

## 🧠 Temel Özellikler ve Modüller

### 📊 Modül 1: Visual Prototyping & Flowwise AI

- Docker ile Flowwise AI kurulumu
- LangChain temel bileşenleri
- `ChatPromptTemplate`, `SystemMessage` ve `HumanMessage`
- Prompt Chaining
- ReAct ajanları
- Brave Search API ve Calculator araçları

### ⚡ Modül 2: Production-Grade LCEL & Chainlit

- LangChain Expression Language (LCEL)
- `|` operatörü ile zincir oluşturma
- Asenkron veri akışı
- Neo4j ile Graph Memory
- Chainlit tabanlı sohbet arayüzü
- PostgreSQL / AsyncPG ile veri kalıcılığı
- Literal AI ile gözlemlenebilirlik

### 🔍 Modül 3: Advanced RAG

- Recursive Text Chunking
- SHA-256 ile veri tekrarlarının önlenmesi
- ChromaDB ile vektör arama
- Cosine Similarity
- Halüsinasyonları azaltmaya yönelik Strict Grounding

### 🏠 Modül 4: Local LLM & Ollama

- Yerel LLM çalıştırma
- Ollama entegrasyonu
- GPU destekli inference
- Modelfile kullanımı
- `num_ctx`, `temperature`, `top_p` ve `SYSTEM` parametreleri
- Hassas veriler için yerel inference yaklaşımı

---

## 🛠 Teknoloji Yığını

| Kategori | Teknolojiler |
|---|---|
| Orkestrasyon / Core | LangChain v0.3, LCEL |
| Kullanıcı Arayüzü | Chainlit, Flowwise AI |
| Model Sunucuları | Ollama, Groq, Anthropic Claude, OpenAI |
| Vektör & Graph DB | ChromaDB, Neo4j, PostgreSQL |
| Veri Katmanı | SQLAlchemy, AsyncPG |
| İzlenebilirlik | Literal AI, LangSmith |
| Konteynerizasyon | Docker, Docker Compose |

---

## 📂 Proje Dizini

```text
.
├── 01_flowwise_prototyping/       # Flowwise AI Docker Compose ve yapılandırmaları
├── 02_lcel_chainlit_app/          # LCEL, Chainlit, PostgreSQL ve Authentication
│   ├── app.py                     # Ana Chainlit uygulaması
│   ├── custom_data_layer.py       # Custom SQL Data Layer sınıfları
│   └── chainlit.md                # UI karşılama ekranı
├── 03_rag_chromadb/               # Advanced RAG, Chunking ve ChromaDB
│   ├── pdf_rag_app.py             # PDF yüklemeli RAG uygulaması
│   └── docs/                      # Örnek test belgeleri
├── 04_local_llm_ollama/           # Local LLM, Modelfile ve Ollama
│   ├── Modelfile                  # Özel LLM yapılandırması
│   └── local_chain.py             # LangChain + ChatOllama
├── docker-compose.yml             # PostgreSQL, Neo4j ve Flowwise servisleri
├── requirements.txt               # Python bağımlılıkları
└── README.md                      # Proje dokümantasyonu
```

---

## 🚀 Kurulum ve Hızlı Başlangıç

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/Rasittekin18/Building-AI-Applications-with-LangChain-LLMs.git
cd Building-AI-Applications-with-LangChain-LLMs
```

### 2. Sanal Ortam Oluşturun

```bash
python -m venv venv
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Çevre Değişkenlerini Yapılandırın

Proje kök dizininde `.env` dosyası oluşturun:

```env
ANTHROPIC_API_KEY=your_anthropic_key
OPENAI_API_KEY=your_openai_key
LITERAL_API_KEY=your_literal_ai_key

DATABASE_URL=postgresql+asyncpg://postgres:admin_password@localhost:5432/chainlit_db

NEO4J_URL=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password
```

> **Not:** `.env` dosyanızı GitHub'a yüklemeyin. API anahtarlarınızı gizli tutun.

### 5. Docker Servislerini Başlatın

PostgreSQL, Neo4j ve Flowwise servislerini başlatmak için:

```bash
docker-compose up -d
```

### 6. Chainlit Uygulamasını Çalıştırın

```bash
chainlit run 02_lcel_chainlit_app/app.py -w
```

### 7. Ollama Modelini Çalıştırın

```bash
cd 04_local_llm_ollama

ollama create cybersec-llama3 -f Modelfile

python local_chain.py
```

---


---

## 📄 Lisans

Bu proje **MIT Lisansı** kapsamında lisanslanmıştır.
