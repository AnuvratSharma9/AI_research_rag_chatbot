from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_community.embeddings import FastEmbedEmbeddings 
import os

load_dotenv()
app = FastAPI()

pdf_files = [
    "data/attention.pdf",
    "data/rag.pdf",
    "data/react.pdf",
    "data/cot.pdf",
    "data/llama2.pdf"
]

documents = []
for file in pdf_files:
    loader = PyPDFLoader(file)
    docs = loader.load()
    documents.extend(docs)
    print(f"Loaded {len(documents)} documents")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)
print(f"\nCreated {len(chunks)} chunks")

embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")  

vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 8})

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)
chat_history = []

class query_request(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "AI Research Assistant API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(request: query_request):
    query = request.question

    retrieved_docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    history_text = "\n".join(chat_history[-6:])

    prompt = f"""
    You are an AI Research Assistant built on 5 foundational AI research papers.
    Your job is to:
    - answer questions about AI research papers
    - explain concepts clearly and concisely
    - respond naturally to greetings and casual conversation
    - Answer all parts of the user's question if relevant information exists in the context.
    Rules:
    - If the user greets you, respond warmly and ask how you can help.
    - If the user asks casual conversation unrelated to research, respond briefly and naturally.
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

    response = llm.invoke(prompt)
    answer = response.text

    chat_history.append(f"User:{query}")
    chat_history.append(f"Answer:{answer}")
    if len(chat_history) > 20:
        chat_history.pop(0)

    return {
        "question": query,
        "answer": answer
    }