# AI Document Chatbot (RAG)
### LangChain + FAISS + OpenRouter + Streamlit

🚀 An AI-powered document chatbot that allows users to **upload a file and ask questions about it** using Retrieval-Augmented Generation (RAG).

The system retrieves relevant information from the uploaded document and generates accurate answers using an LLM.

---

## ✨ Features

- 📄 Upload your own text document
- 💬 Chat-style interface (like ChatGPT)
- 🔍 Semantic search using embeddings
- 🧠 Answers generated using LLM (Llama 3 via OpenRouter)
- ⚡ Fast retrieval using FAISS vector database
- 🌐 Interactive web app using Streamlit

---

## 🛠 Tech Stack

- Python
- LangChain
- FAISS (Vector Database)
- OpenRouter API
- Llama 3
- Streamlit

---

## 📂 Project Structure

```
rag-document-chatbot
│
├── app.py              # Streamlit web app (UI + chat)
├── main.py             # RAG pipeline (backend logic)
├── data.txt            # Sample document
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

```
User uploads file
        ↓
Text is split into chunks
        ↓
Chunks → embeddings
        ↓
Stored in FAISS vector database
        ↓
User asks question
        ↓
Retriever finds relevant chunks
        ↓
Context sent to LLM
        ↓
LLM generates answer
        ↓
Answer displayed in chat UI
```

This ensures answers are based on the **uploaded document**, not general AI knowledge.

---

## 🚀 Installation

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

---

## ▶️ Run the App

```
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 💡 Example Usage

1. Upload a `.txt` file  
2. Ask a question like:

```
What is machine learning?
```

3. The chatbot will answer based on the document

---

## 🧠 Learning Concepts

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings
- Semantic search
- LLM integration
- Building AI web apps with Streamlit

---

## 🚀 Future Improvements

- 📄 PDF support
- 📂 Multiple file upload
- 💾 Persistent vector database
- 🌐 Deploy online (public access)
- 🎨 Improved UI/UX

---

## 👨‍💻 Author

**Pranav Agarwal**

GitHub:  
https://github.com/agarwalpranav0711