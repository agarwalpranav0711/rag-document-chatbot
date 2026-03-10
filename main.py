from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

# Load document
loader = TextLoader("data.txt")
documents = loader.load()

# Split text into chunks
text_splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

docs = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings(
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1"
)

# Store vectors
vectorstore = FAISS.from_documents(docs, embeddings)

# Create retriever
retriever = vectorstore.as_retriever()

# Create LLM
llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3-8b-instruct"
)

# Ask question
query = "What is machine learning?"

# Retrieve relevant document
relevant_docs = retriever.invoke(query)

context = relevant_docs[0].page_content

prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)

print(response.content)