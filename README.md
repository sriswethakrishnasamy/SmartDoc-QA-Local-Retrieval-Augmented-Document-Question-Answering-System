📄 Offline Document Question Answering System using RAG
📌 Project Overview
This project implements an offline-capable Document Question Answering system using Retrieval-Augmented Generation (RAG). The system allows users to upload documents in PDF, DOCX, or TXT format, ask questions in natural language, and receive accurate answers derived only from the document content, without using any cloud-based APIs.
All processing — embedding generation, document retrieval, and question answering — is performed locally, making the system secure, private, and suitable for offline environments.

🎯 Project Objective
To build an intelligent, offline document-based question answering system that:
Accepts multiple document formats (PDF, DOCX, TXT)
Uses semantic search to retrieve relevant document sections
Generates accurate answers using a local NLP model
Works completely offline without relying on cloud services

🧠 Key Features
📂 Upload documents (PDF, DOCX, TXT)
🔍 Semantic document retrieval using vector embeddings
🤖 Question answering using pretrained NLP models
📴 Fully offline (no OpenAI / cloud APIs)
🖥️ Simple and interactive Streamlit UI

🛠️ Technologies & Libraries Used
Programming Language: Python
Frontend: Streamlit
Embedding Model: Sentence Transformers (all-MiniLM-L6-v2)
Vector Database: FAISS
Question Answering Model: deepset/roberta-base-squad2
Document Processing:
pypdf – PDF reading
python-docx – DOCX reading
Core Libraries: NumPy, Transformers

⚙️ System Architecture / Workflow

Document Upload

User uploads a PDF, DOCX, or TXT file via Streamlit UI
Text Extraction
PDF → pypdf
DOCX → python-docx
TXT → UTF-8 decoding
Text Chunking
Document text is split into fixed-size chunks (1000 characters)
Embedding Generation
Sentence embeddings are created using all-MiniLM-L6-v2
Vector Storage
FAISS index stores embeddings for fast similarity search
Query Processing
User question is embedded
Top relevant chunks are retrieved using FAISS
Answer Generation
Retrieved context is passed to a local QA model
Final answer is extracted from the document context

📂 Project Structure
├── app.py          # Streamlit application
├── rag_local.py    # RAG logic (embeddings, FAISS, QA)
├── utils.py        # Document loading utilities
├── README.md       # Project documentation

📊 Model Details
Embedding Model: all-MiniLM-L6-v2
QA Model: deepset/roberta-base-squad2
Retrieval Method: FAISS (L2 distance)
Answering Approach: Extractive Question Answering

🚀 Use Cases
Academic document analysis
Legal or policy document querying
Offline knowledge assistants
Secure document understanding systems
