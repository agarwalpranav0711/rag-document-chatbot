from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS


def load_documents(file_path: str):
    """Load documents from a text file."""
    loader = TextLoader(file_path)
    return loader.load()


def split_documents(documents):
    """Split documents into smaller chunks."""
    splitter = CharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    return splitter.split_documents(documents)


def create_vectorstore(docs, api_key):
    """Create embeddings and store them in FAISS."""
    embeddings = OpenAIEmbeddings(
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1"
    )

    return FAISS.from_documents(docs, embeddings)


def create_llm(api_key):
    """Initialize the language model."""
    return ChatOpenAI(
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1",
        model="meta-llama/llama-3-8b-instruct"
    )


def main():
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")

    # Load and process document
    documents = load_documents("data.txt")
    docs = split_documents(documents)

    # Create vector database
    vectorstore = create_vectorstore(docs, api_key)
    retriever = vectorstore.as_retriever()

    # Create LLM
    llm = create_llm(api_key)

    query = "What is machine learning?"

    # Retrieve context
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

    print("\nAnswer:")
    print(response.content)


if __name__ == "__main__":
    main()