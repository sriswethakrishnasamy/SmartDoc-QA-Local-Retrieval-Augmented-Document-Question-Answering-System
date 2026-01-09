import streamlit as st
from utils import load_pdf, load_docx, load_txt
from rag_local import create_vector_store, retrieve_answer

st.title("📄 Local Document Q&A with RAG")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])
question = st.text_input("Ask a question about the document")

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = load_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        text = load_docx(uploaded_file)
    else:
        text = load_txt(uploaded_file)

    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    index, embeddings, chunk_texts = create_vector_store(chunks)

    if question:
        answer = retrieve_answer(question, index, embeddings, chunk_texts)
        st.markdown(f"**Answer:** {answer}")
