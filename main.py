from dotenv import load_dotenv
import os
import whisper
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS

# -----------------------------
# Load environment
# -----------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# -----------------------------
# Load Documents
# -----------------------------
def load_documents(file_path: str):
    """Load documents from TXT, PDF, or AUDIO"""

    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        docs = [doc for doc in docs if doc.page_content.strip() != ""]
        return docs

    elif file_path.endswith(".mp3") or file_path.endswith(".wav"):
        return load_audio(file_path)

    else:
        loader = TextLoader(file_path)
        return loader.load()

def load_audio(file_path: str):
    """Convert audio file to Document using Whisper"""

    model = whisper.load_model("tiny")  # fast model
    result = model.transcribe(file_path)

    text = result["text"]

    # 🚨 IMPORTANT: convert to Document
    if text.strip() == "":
        return []

    return [Document(page_content=text)]


# -----------------------------
# Split Documents
# -----------------------------
def split_documents(documents):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


# -----------------------------
# Vector Store
# -----------------------------
def create_vectorstore(docs, api_key):
    embeddings = OpenAIEmbeddings(
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1"
    )

    return FAISS.from_documents(docs, embeddings)


# -----------------------------
# LLM
# -----------------------------
def create_llm(api_key, model_name):
    return ChatOpenAI(
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1",
        model=model_name,
        max_tokens=300  # 🔥 LIMIT COST
    )