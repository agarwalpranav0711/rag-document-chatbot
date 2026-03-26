# 📚 AI Study Assistant (RAG)

### LangChain + FAISS + OpenRouter + Streamlit

🚀 An AI-powered document chatbot that allows users to **upload TXT or PDF files and interact with them** using Retrieval-Augmented Generation (RAG).

It retrieves relevant information from the document and generates accurate, context-aware answers using LLMs.

---

## ✨ Features

* 📄 Upload **TXT & PDF documents**
* 💬 Chat with your document (ChatGPT-style UI)
* 🧠 Conversation memory (context-aware answers)
* 🔍 Semantic search using embeddings
* 🤖 Multi-model support (Llama 3, Mixtral)
* 📘 One-click document summary
* ⚡ Fast retrieval using FAISS
* 🌐 Interactive web UI with Streamlit

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
├── app.py              # Streamlit UI (chat + summary)
├── main.py             # RAG backend logic
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
Text split into chunks
        ↓
Embeddings created
        ↓
Stored in FAISS
        ↓
User asks question
        ↓
Retriever finds context
        ↓
Context + chat history → LLM
        ↓
LLM generates answer
```

👉 Ensures answers are based on **your document**, not general AI knowledge.

---

## 🚀 Installation

```bash
git clone https://github.com/agarwalpranav0711/rag-document-chatbot.git
cd rag-document-chatbot
pip install -r requirements.txt
```

Create `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

## 💡 Example Usage

1. Upload a `.txt` or `.pdf` file
2. Ask:

```
What is machine learning?
```

3. Follow-up:

```
Explain more
```

4. Generate summary
5. Switch models and compare responses

---

## 🧠 What You Learn

* RAG (Retrieval-Augmented Generation)
* Vector embeddings & semantic search
* LLM integration
* Chat memory systems
* Multi-model AI usage
* Building AI web apps

---

## 🚀 Future Improvements

* 📂 Multi-file support
* 💾 Persistent vector database
* 📄 Show source references
* 🎨 UI improvements
* 🌐 Public deployment
* 🖼️ Multimodal support

---

## 👨‍💻 Author

**Pranav Agarwal**

GitHub:
https://github.com/agarwalpranav0711
