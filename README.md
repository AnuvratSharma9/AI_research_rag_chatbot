# AI Research Assistant

A conversational Retrieval-Augmented Generation (RAG) application built using FastAPI, Streamlit, FAISS, Hugging Face embeddings, and Gemini.

The assistant performs semantic retrieval over 5 foundational AI research papers and generates grounded responses using retrieved context.

---

# Features

- Conversational AI Research Assistant
- Multi-document RAG pipeline
- Semantic search using vector embeddings
- FAISS vector database
- FastAPI backend API
- Streamlit frontend UI
- Conversational memory
- Grounded AI responses
- Research-paper-based retrieval
- Multi-paper semantic question answering

---

# Research Papers Used

The assistant retrieves information from the following foundational AI papers:

1. Attention Is All You Need
2. Retrieval-Augmented Generation (RAG)
3. Chain-of-Thought Prompting
4. Llama 2
5. ReAct

These papers provide knowledge related to:

- Transformers
- Self-attention
- Retrieval-Augmented Generation
- Prompt engineering
- AI agents
- LLM training
- Reasoning systems

---

# Tech Stack

## Frontend

- Streamlit

## Backend

- FastAPI
- Uvicorn

## AI / RAG Components

- LangChain
- Hugging Face Embeddings
- Gemini 2.5 Flash
- FAISS Vector Store
- Sentence Transformers

## Embedding Model

- sentence-transformers/all-MiniLM-L6-v2

---

# System Architecture

```text
Research Papers
        ↓
Document Loader
        ↓
Text Splitter
        ↓
Embeddings
        ↓
FAISS Vector Store
        ↓
Retriever
        ↓
Prompt Construction
        ↓
Gemini LLM
        ↓
Final Response
```

---

# How the RAG Pipeline Works

## 1. Document Loading

PDF research papers are loaded using PyPDFLoader.

## 2. Text Splitting

Documents are split into smaller chunks using RecursiveCharacterTextSplitter.

## 3. Embedding Generation

Each chunk is converted into vector embeddings using Hugging Face sentence transformers.

## 4. Vector Storage

The embeddings are stored inside a FAISS vector database.

## 5. Semantic Retrieval

When a user asks a question:

- the query is converted into embeddings
- semantic similarity search is performed
- relevant chunks are retrieved

## 6. Prompt Injection

Retrieved chunks + conversation history are injected into the final LLM prompt.

## 7. Response Generation

Gemini generates a grounded response based only on the retrieved context.

---

# Project Structure

```text
AI-Research-Assistant/
│
├── data/
│   ├── attention.pdf
│   ├── rag.pdf
│   ├── react.pdf
│   ├── cot.pdf
│   └── llama2.pdf
│
├── backend.py
├── frontend.py
├── requirements.txt
├── .env
├── README.md
└── LICENSE
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd AI-Research-Assistant
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Libraries

```bash
pip install fastapi uvicorn streamlit requests
pip install langchain langchain-community
pip install langchain-google-genai
pip install langchain-huggingface
pip install sentence-transformers
pip install faiss-cpu
pip install pypdf
pip install python-dotenv
```

---

# Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

# Running the Backend

```bash
uvicorn backend:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

Open another terminal:

```bash
streamlit run frontend.py
```

---

# Example Questions

## Transformers

- What is self-attention?
- What is multi-head attention?
- Why are transformers better than RNNs?

## RAG

- How does Retrieval-Augmented Generation work?
- How does RAG reduce hallucinations?

## LLMs

- How was Llama 2 trained?
- What is RLHF?

## Agents

- What is ReAct?
- How do ReAct agents combine reasoning and acting?

## Prompt Engineering

- What is chain-of-thought prompting?
- How does chain-of-thought improve reasoning?

---

# Conversational Memory

The application includes conversational memory by storing recent chat history and injecting it into the prompt.

This enables:

- follow-up questions
- contextual conversations
- multi-turn interactions

Example:

```text
User: What is self-attention?
User: Why is it important?
```

The assistant understands that “it” refers to self-attention.

---

# Key Concepts Demonstrated

This project demonstrates understanding of:

- Retrieval-Augmented Generation (RAG)
- Semantic search
- Vector databases
- Embeddings
- Cosine similarity
- Prompt engineering
- LLM integration
- FastAPI APIs
- Streamlit UI development
- Conversational AI systems

---

# Future Improvements

Potential future upgrades:

- Source citations
- Async backend
- Streaming responses
- Hybrid retrieval
- Query reformulation
- Reranking
- Qdrant / Pinecone support
- LangGraph integration
- Docker deployment
- Persistent memory storage

---

# Deployment

## Backend Deployment

Suggested:

- Render
- Railway

## Frontend Deployment

Suggested:

- Streamlit Community Cloud

---

# Resume Description

Built a conversational AI Research Assistant using Retrieval-Augmented Generation (RAG), semantic vector search, FAISS, Hugging Face embeddings, FastAPI, Streamlit, and Gemini LLMs to perform grounded multi-document question answering over foundational AI research papers.

---

# Screenshots

Add screenshots of:

- chat interface
- retrieval examples
- deployed application
- semantic question answering

---

# License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# Author

Built by Anuvrat Sharma.

