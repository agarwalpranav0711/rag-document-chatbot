import streamlit as st
from main import ask_question

# Title
st.title("AI Document Chatbot")

# Description
st.write("Ask a question about your document")

# Input box
question = st.text_input("Enter your question:")

# Button
if st.button("Submit"):

    if question.strip() != "":

        with st.spinner("Thinking..."):
            answer = ask_question(question)

        st.write("Answer:")
        st.success(answer)

    else:
        st.warning("Please enter a question.")