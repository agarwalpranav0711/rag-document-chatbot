# Simple RAG System (LangChain + OpenRouter)

This project implements a basic Retrieval-Augmented Generation (RAG) pipeline.

## Features

- Load document
- Split text into chunks
- Create embeddings
- Store vectors using FAISS
- Retrieve relevant context
- Generate answers using LLM

## Tech Stack

- Python
- LangChain
- FAISS
- OpenRouter
- Llama 3

## How it Works

User Question  
↓  
Vector Search  
↓  
Relevant Context  
↓  
LLM Generates Answer

## Run the Project

Install dependencies:

pip install -r requirements.txt

Create `.env` file:

OPENROUTER_API_KEY=your_key_here

Run:

python main.py