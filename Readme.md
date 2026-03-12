# Simple RAG System (LangChain + OpenRouter)

This project demonstrates a basic **Retrieval-Augmented Generation (RAG)** pipeline using LangChain, FAISS, and an LLM accessed via OpenRouter.

## Features

* Load documents from a text file
* Split text into smaller chunks
* Generate embeddings
* Store embeddings in a FAISS vector database
* Retrieve relevant context for a user query
* Generate answers using an LLM

## Tech Stack

* Python
* LangChain
* FAISS
* OpenRouter
* Llama 3

## Project Structure

```
rag-document-chatbot
│
├── rag_pipeline.py
├── data.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

```
User Question
      ↓
Vector Search (FAISS)
      ↓
Retrieve Relevant Text
      ↓
Send Context + Question to LLM
      ↓
Generate Answer
```

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

Create a `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

## Run the Project

```
python rag_pipeline.py
```

## Example Query

Question:

```
What is machine learning?
```

Answer:

```
Machine learning is a subset of AI that allows systems to learn from data.
```