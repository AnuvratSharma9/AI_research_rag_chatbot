from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import  ChatGoogleGenerativeAI
import os

load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")
app=FastAPI()


pdf_files = [
    "data/attention.pdf",
    "data/rag.pdf",
    "data/react.pdf",
    "data/cot.pdf",
    "data/llama2.pdf"
]

documents=[]
#loading documents
for file in pdf_files:

    loader=PyPDFLoader(file)
    docs=loader.load()
    documents.extend(docs) # it adds one document whch is a page into the empty documents list 
    print(f"Loaded {len(documents)} documents")

#text splitting
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
chunks=text_splitter.split_documents(documents)
print(f"\nCreated {len(chunks)} chunks")

#embeddings
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#vector Store
vectorstore=FAISS.from_documents(chunks,embeddings)
#chunks and embeddings are stored

#RETRIEVER
retriever =vectorstore.as_retriever(
    search_kwargs={"k": 8}
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=api_key,
    temperature=0.3
)

chat_history = [] # memory


class query_request(BaseModel):
    question:str

@app.get("/")
def home():

    return {
        "message": "AI Research Assistant API Running"
    }

@app.post("/chat")
def chat(request:query_request):

    query=request.question
    #RETRIEVE
    retrieved_docs=retriever.invoke(query)

    context="/n/n".join(
        [doc.page_content for doc in retrieved_docs ]
    )


    history_text = "\n".join(
        chat_history[-6:]
    )

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

    response=llm.invoke(prompt)
    answer=response.text

    chat_history.append(f"User:{query}")
    chat_history.append(f"Answer:{answer}")

    if len(chat_history) >20:
        chat_history.pop(0)

    return {
        "question": query,
        "answer": answer
    }