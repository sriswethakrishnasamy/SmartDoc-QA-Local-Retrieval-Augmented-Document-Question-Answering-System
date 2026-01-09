from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np

embedder = SentenceTransformer("all-MiniLM-L6-v2")
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

def create_vector_store(chunks):
    embeddings = embedder.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings, chunks

def retrieve_answer(question, index, embeddings, chunks, top_k=3):
    q_embed = embedder.encode([question])
    _, indices = index.search(np.array(q_embed), top_k)
    context = " ".join([chunks[i] for i in indices[0]])
    result = qa_model(question=question, context=context)
    return result["answer"]
