# 🧠 AI Research Assistant

An intelligent RAG-powered chatbot built using Streamlit, LangChain, Groq, and foundational AI research papers.

The application allows users to ask questions about influential AI papers and receive contextual answers generated using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- Chat with 5 foundational AI research papers
- Retrieval-Augmented Generation (RAG)
- Semantic document search using FAISS
- Conversational memory
- Real-time streaming responses
- Interactive Streamlit interface
- Groq-powered LLM inference
- Source-aware responses

---

## 📚 Research Papers Included

The assistant is built on the following papers:

### 1. Attention Is All You Need
Introduced the Transformer architecture and self-attention mechanism.

### 2. Retrieval-Augmented Generation (RAG)
Combines external knowledge retrieval with language models.

### 3. Chain-of-Thought Prompting
Improves reasoning performance through intermediate reasoning steps.

### 4. ReAct
Combines reasoning and action generation in language models.

### 5. Llama 2
Meta's open-source family of large language models.

---

## 🏗️ Architecture

```text
PDF Research Papers
          │
          ▼
 Document Loading
(PyMuPDFLoader)
          │
          ▼
 Text Chunking
(RecursiveCharacterTextSplitter)
          │
          ▼
 Embedding Generation
(all-MiniLM-L6-v2)
          │
          ▼
 FAISS Vector Store
          │
          ▼
 Relevant Context Retrieval
          │
          ▼
 Groq LLM
(Llama 3.3 70B)
          │
          ▼
 Streamlit Chat Interface
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### LLM
- Groq
- Llama 3.3 70B Versatile

### Retrieval
- LangChain
- FAISS

### Embeddings
- Sentence Transformers
- all-MiniLM-L6-v2

### PDF Processing
- PyMuPDF

### Language
- Python

---

## 📂 Project Structure

```text
AI-Research-RAG-Chatbot/
│
├── frontend.py
├── requirements.txt
│
├── data/
│   ├── attention.pdf
│   ├── rag.pdf
│   ├── react.pdf
│   ├── cot.pdf
│   └── llama2.pdf
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Research-RAG-Chatbot.git
cd AI-Research-RAG-Chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com

---

## ▶️ Run Application

```bash
streamlit run frontend.py
```

Application will start on:

```text
http://localhost:8501
```

---

## 💬 Example Questions

- What problem does RAG solve?
- How does self-attention work in Transformers?
- Explain the ReAct framework.
- What are the advantages of Chain-of-Thought prompting?
- What improvements were introduced in Llama 2?

---

## 🎯 Key Learnings

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Embedding Models
- Conversational AI
- Prompt Engineering
- Document Question Answering
- Streamlit Deployment
- LangChain Workflows

---

## 🔮 Future Improvements

- PDF Upload Support
- Citation-Based Answers
- Multi-PDF Knowledge Bases
- Hybrid Search
- Persistent Chat Memory
- User Authentication
- Cloud Deployment
- Multi-Agent Research Workflows

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Anuvrat Sharma

Focused on Machine Learning, Data Science, Generative AI, and AI Engineering.
