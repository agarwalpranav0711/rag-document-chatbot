# AI Document Chatbot (RAG)
### LangChain + FAISS + OpenRouter + Streamlit

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about a document through a **web interface**.

The system searches the document for relevant context using **vector embeddings** and generates answers using an **LLM via OpenRouter**.

---

## Features

- Load documents from a text file
- Split text into smaller chunks
- Generate embeddings
- Store embeddings in a FAISS vector database
- Retrieve relevant context for a user query
- Generate answers using an LLM
- Interactive **Streamlit web interface**

---

## Tech Stack

- Python
- LangChain
- FAISS (Vector Database)
- OpenRouter API
- Llama 3
- Streamlit

---

## Project Structure

```
rag-document-chatbot
│
├── app.py              # Streamlit UI
├── main.py             # RAG pipeline
├── data.txt            # Example document
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How the System Works

```
User Question
      ↓
Streamlit UI
      ↓
Retriever (FAISS Vector Search)
      ↓
Retrieve Relevant Document Chunks
      ↓
Send Context + Question to LLM
      ↓
Generate Answer
      ↓
Display in UI
```

This approach allows the LLM to answer questions **based on your document instead of general knowledge**.

---

## Installation

Clone the repository:

```
git clone https://github.com/agarwalpranav0711/rag-document-chatbot.git
cd rag-document-chatbot
```

Install dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

## Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

---

## Example Query

Question:

```
What is machine learning?
```

Answer:

```
Machine learning is a subset of AI that allows systems to learn from data.
```

---

## Learning Goals

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings
- Semantic search
- LLM integration
- Building AI web apps with Streamlit

---

## Future Improvements

- Chat-style interface
- Support for PDF documents
- Upload documents via UI
- Persistent vector database
- Multi-document search

---

## Author

**Pranav Agarwal**

GitHub:  
https://github.com/agarwalpranav0711