# AI Document Chatbot (RAG)

### LangChain + FAISS + OpenRouter + Streamlit

🚀 An AI-powered document chatbot that allows users to **upload TXT or PDF files and ask questions about them** using Retrieval-Augmented Generation (RAG).

The system retrieves relevant information from the uploaded document and generates accurate answers using an LLM.

---

## ✨ Features

* 📄 Upload **TXT and PDF documents**
* 💬 Chat-style interface (like ChatGPT)
* 🧠 Conversation memory (context-aware responses)
* 🔍 Semantic search using embeddings
* 🤖 Multi-model support (switch between models)
* ⚡ Fast retrieval using FAISS vector database
* 🌐 Interactive web app using Streamlit

---

## 🛠 Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* OpenRouter API
* Llama 3 / Mixtral
* Streamlit

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
User uploads file (TXT / PDF)
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
Context + chat history sent to LLM
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

1. Upload a `.txt` or `.pdf` file
2. Ask a question like:

```
What is machine learning?
```

3. Ask follow-up questions:

```
Explain more
```

4. Switch models and compare answers

---

## 🧠 Learning Concepts

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector embeddings
* Semantic search
* LLM integration
* Conversational memory
* Multi-model AI systems
* Building AI web apps with Streamlit

---

## 🚀 Future Improvements

* 📂 Multiple file upload
* 💾 Persistent vector database
* 📄 Show source references (page/chunk)
* 🎨 Improved UI/UX
* 🌐 Deploy online (public access)
* 🖼️ Multimodal support (images)

---

## 👨‍💻 Author

**Pranav Agarwal**

GitHub:
https://github.com/agarwalpranav0711
