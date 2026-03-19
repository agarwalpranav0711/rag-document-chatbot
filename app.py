import streamlit as st
import os
from dotenv import load_dotenv

from main import load_documents, split_documents, create_vectorstore, create_llm

# Load API key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

st.title("AI Document Chatbot")

# Model selector
model_option = st.selectbox(
    "Choose AI Model",
    [
        "meta-llama/llama-3-8b-instruct",
        "mistralai/mixtral-8x7b-instruct"
    ]
)

# -------------------------------
# File Upload
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload a file",
    type=["txt", "pdf"]
)

if uploaded_file is not None:

    # Save file with correct extension
    file_path = f"uploaded.{uploaded_file.name.split('.')[-1]}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully!")

    # Reset chat when new file uploaded
    st.session_state.messages = []

    # Process file
    documents = load_documents(file_path)
    docs = split_documents(documents)

    vectorstore = create_vectorstore(docs, api_key)
    retriever = vectorstore.as_retriever()

    st.session_state.retriever = retriever

# -------------------------------
# Chat Interface
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Ask a question about your document")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):

        if "retriever" in st.session_state:

            with st.spinner("Thinking..."):

                relevant_docs = st.session_state.retriever.invoke(user_input)
                context = "\n".join([doc.page_content for doc in relevant_docs])

                # Memory
                chat_history = ""
                for msg in st.session_state.messages:
                    chat_history += f"{msg['role']}: {msg['content']}\n"

                prompt = f"""
You are a helpful AI assistant.

Conversation history:
{chat_history}

Context:
{context}

User question:
{user_input}
"""

                llm = create_llm(api_key, model_option)
                response = llm.invoke(prompt)
                answer = response.content

        else:
            answer = "Please upload a file first."

        st.markdown(f"🤖 **Model:** `{model_option}`")
        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"[{model_option}] {answer}"
    })