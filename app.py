import streamlit as st
import os
import time
from dotenv import load_dotenv

from main import load_documents, split_documents, create_vectorstore, create_llm

# -----------------------------
# Config
# -----------------------------
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# -----------------------------
# Usage Control (🔥 IMPORTANT)
# -----------------------------
if "query_count" not in st.session_state:
    st.session_state.query_count = 0

MAX_QUERIES = 10

if "last_query_time" not in st.session_state:
    st.session_state.last_query_time = 0

# -----------------------------
# Header
# -----------------------------
st.markdown("# 📚 AI Study Assistant")
st.caption("Upload notes → Ask questions → Get smart answers instantly 🚀")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    model_option = st.selectbox(
        "Choose AI Model",
        [
            "meta-llama/llama-3-8b-instruct",
            "mistralai/mixtral-8x7b-instruct"
        ]
    )

    uploaded_file = st.file_uploader(
        "Upload file",
        type=["txt", "pdf"]
    )

# -----------------------------
# File Processing
# -----------------------------
if uploaded_file is not None:

    file_path = f"uploaded.{uploaded_file.name.split('.')[-1]}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.toast("File uploaded successfully ✅")
    st.caption(f"📄 Loaded: {uploaded_file.name}")

    # reset chat
    st.session_state.messages = []
    st.session_state.summary = None

    with st.spinner("Processing document..."):
        documents = load_documents(file_path)
        docs = split_documents(documents)

    if len(docs) == 0:
        st.error("No readable content found ❌")
        st.stop()

    vectorstore = create_vectorstore(docs, api_key)
    retriever = vectorstore.as_retriever()
    llm = create_llm(api_key, model_option)

    st.session_state.retriever = retriever
    st.session_state.llm = llm
    st.session_state.docs = docs

# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns([2, 1])

# =============================
# CHAT
# =============================
with col1:

    st.markdown("### 💬 Chat with your document")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "👋 Upload a document and start asking questions!"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    st.divider()

    user_input = st.chat_input("Ask anything about your document...")

    if user_input:

        # 🔥 LIMIT CHECK
        if st.session_state.query_count >= MAX_QUERIES:
            st.warning("⚠️ Free limit reached. Refresh to continue.")
            st.stop()

        # 🔥 RATE LIMIT
        if time.time() - st.session_state.last_query_time < 3:
            st.warning("⏳ Please wait before next request")
            st.stop()

        st.session_state.last_query_time = time.time()
        st.session_state.query_count += 1

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):

            if "retriever" in st.session_state:

                with st.spinner("Thinking..."):

                    relevant_docs = st.session_state.retriever.invoke(user_input)

                    # 🔥 LIMIT CONTEXT (COST CONTROL)
                    context = "\n".join(
                        [doc.page_content for doc in relevant_docs[:3]]
                    )

                    chat_history = ""
                    for msg in st.session_state.messages:
                        chat_history += f"{msg['role']}: {msg['content']}\n"

                    prompt = f"""
You are an AI Study Assistant.

Explain clearly like a teacher.

Conversation history:
{chat_history}

Context:
{context}

User question:
{user_input}
"""

                    response = st.session_state.llm.invoke(prompt)
                    answer = response.content

            else:
                answer = "Please upload a file first."

            st.markdown(f"🤖 **Model:** `{model_option}`")
            st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": f"[{model_option}] {answer}"}
        )

# =============================
# SUMMARY
# =============================
with col2:

    st.markdown("### 📘 Document Summary")

    if "docs" in st.session_state:

        if st.button("✨ Generate Summary", use_container_width=True):

            # 🔥 LIMIT CHECK
            if st.session_state.query_count >= MAX_QUERIES:
                st.warning("⚠️ Limit reached.")
                st.stop()

            st.session_state.query_count += 1

            with st.spinner("Generating summary..."):

                # 🔥 LIMIT TEXT SIZE
                full_text = "\n".join(
                    [doc.page_content for doc in st.session_state.docs[:10]]
                )

                prompt = f"""
Summarize the following document in simple terms:

{full_text}
"""

                response = st.session_state.llm.invoke(prompt)
                summary = response.content
                st.session_state.summary = summary

                st.markdown(
                    f"""
                    <div style="
                        background-color:#1e293b;
                        padding:20px;
                        border-radius:12px;
                        border:1px solid #334155;
                        font-size:14px;
                        line-height:1.6;
                    ">
                    {summary}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    else:
        st.info("Upload a file to enable summary.")