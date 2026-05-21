import os
from dotenv import load_dotenv
import streamlit as st

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import time
load_dotenv()

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Research Assistant")
st.markdown("Ask questions about foundational AI research papers.")
st.info("""
📚 Powered by 5 foundational AI research papers:

- Attention Is All You Need  
- Retrieval-Augmented Generation (RAG)  
- Chain-of-Thought Prompting  
- Llama 2  
- ReAct
""")

pdf_files = [
    "data/attention.pdf",
    "data/rag.pdf",
    "data/react.pdf",
    "data/cot.pdf",
    "data/llama2.pdf"
]

@st.cache_resource
def load_rag():
    documents = []
    for file in pdf_files:
        loader = PyMuPDFLoader(file)
        docs = loader.load()
        documents.extend(docs)
        print(f"Loaded {len(documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 8})

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.3
    )

    return retriever, llm

with st.spinner("Loading research papers..."):
    retriever, llm = load_rag()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask something about the papers...")

if query:

    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.write(query)

    retrieved_docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    history_text = "\n".join(
        st.session_state.chat_history[-6:]
    )

    prompt = f"""
You are an AI Research Assistant built on 5 foundational AI research papers.

Your job is to:
- Answer questions about AI research papers
- Explain concepts clearly and concisely
- Respond naturally to greetings and casual conversation

Rules:
- If the user greets you, respond warmly.
- For AI research questions, use ONLY the provided context.
- Summarize instead of copying text directly.
- Keep answers concise and clear.
- If the answer is not found in the context, say:
"I don't know based on the research papers provided."

Conversation History:
{history_text}

Context:
{context}

Question:
{query}
"""

    try:

        with st.spinner("Thinking..."):
            response = llm.invoke(prompt)
            answer = response.content

        with st.chat_message("assistant"):

            typing = st.empty()

            for _ in range(2):
                typing.markdown("⬤ ⬤ ⬤")
                time.sleep(0.3)

            typing.empty()

            placeholder = st.empty()

            displayed = ""

            for char in answer:
                displayed += char
                placeholder.markdown(displayed)
                time.sleep(0.005)

        st.session_state.chat_history.append(
            f"User: {query}"
        )

        st.session_state.chat_history.append(
            f"Assistant: {answer}"
        )

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

    except Exception as e:

        st.error(f"Error: {e}")
