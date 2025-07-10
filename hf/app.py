# app.py
import streamlit as st
from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    RagTokenizer,
    RagRetriever,
    RagSequenceForGeneration,
    pipeline
)
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from ner_utils import load_ner_model, predict_ner

# --- Config ---
st.set_page_config(page_title="🇫🇷 Legal Clause Assistant (RAG + NER)", layout="wide")
st.title("🇫🇷 Legal Clause Assistant (RAG + NER)")

# --- RAG Setup ---
@st.cache_resource
def load_faiss_index():
    # Replace with your pre-built FAISS index path (or create one dynamically)
    index = faiss.read_index("path/to/faiss_index.bin")  # Example path
    return index

@st.cache_resource
def load_retriever_model():
    # Bi-encoder for retrieval (e.g., SBERT)
    retriever_model = SentenceTransformer("dangvantuan/sentence-camembert-base")
    return retriever_model

@st.cache_resource
def load_rag_generator():
    # RAG generator (French-optimized)
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="exact")
    generator = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)
    return tokenizer, generator

# --- NER Setup ---
@st.cache_resource
def load_ner_pipeline():
    ner_model, tokenizer = load_ner_model("models/french_ner_model")
    return ner_model, tokenizer

# --- Main App ---
query = st.text_input("Entrez une clause légale en français :")

if query:
    # --- RAG Answer ---
    st.subheader("📌 RAG Answer")
    
    # 1. Retrieve relevant clauses with FAISS
    retriever_model = load_retriever_model()
    query_embedding = retriever_model.encode(query)
    faiss_index = load_faiss_index()
    _, retrieved_indices = faiss_index.search(np.array([query_embedding]), k=3)  # Top 3 results
    
    # 2. Generate answer with RAG
    tokenizer, generator = load_rag_generator()
    inputs = tokenizer(query, return_tensors="pt")
    outputs = generator.generate(input_ids=inputs["input_ids"])
    rag_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.success(rag_answer)

    # --- NER Tagging ---
    st.subheader("📑 NER Clause Tagging")
    ner_model, ner_tokenizer = load_ner_pipeline()
    tags = predict_ner(query, ner_model, ner_tokenizer)
    st.write(tags)