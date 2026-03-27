from dotenv import load_dotenv
import os

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
    """Load documents from TXT or PDF file."""

    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        # remove empty pages
        docs = [doc for doc in docs if doc.page_content.strip() != ""]
    else:
        loader = TextLoader(file_path)
        docs = loader.load()

    return docs


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