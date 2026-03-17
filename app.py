import streamlit as st
import os
from dotenv import load_dotenv

from main import load_documents, split_documents, create_vectorstore, create_llm

# Load API key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

st.title("AI Document Chatbot")

# -------------------------------
# File Upload
# -------------------------------

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:

    # Save uploaded file
    with open("uploaded.txt", "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully!")

    # Process file
    documents = load_documents("uploaded.txt")
    docs = split_documents(documents)

    vectorstore = create_vectorstore(docs, api_key)
    retriever = vectorstore.as_retriever()
    llm = create_llm(api_key)

    # Store in session
    st.session_state.retriever = retriever
    st.session_state.llm = llm

# -------------------------------
# Chat Interface
# -------------------------------

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Ask a question about your document")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate answer
    with st.chat_message("assistant"):

        if "retriever" in st.session_state:

            with st.spinner("Thinking..."):

                relevant_docs = st.session_state.retriever.invoke(user_input)
                context = "\n".join([doc.page_content for doc in relevant_docs])

                prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{user_input}
"""

                response = st.session_state.llm.invoke(prompt)
                answer = response.content

        else:
            answer = "Please upload a file first."

        st.write(answer)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})