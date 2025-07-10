# app.py
import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import spacy
from ner_utils import load_ner_model, predict_ner
import os

st.set_page_config(page_title="Legal-AI FR", layout="wide")
#st.set_page_config(page_title="Legal AI FR", page_icon="⚖️")

st.title("🇫🇷 Legal Clause Assistant (RAG + NER)")
#st.title("⚖️ Legal AI for French Legal Documents")

query = st.text_input("Entrez une clause légale en français :")



if query:
    st.subheader("📌 RAG Answer")
    rag_pipe = pipeline("text2text-generation", model="philschmid/bart-large-cnn-samsum")  # Placeholder RAG
    rag_response = rag_pipe(query, max_length=200, do_sample=False)[0]['generated_text']
    st.success(rag_response)

    st.subheader("📑 NER Clause Tagging")
    ner_model, tokenizer = load_ner_model("models/french_ner_model")
    tags = predict_ner(query, ner_model, tokenizer)
    st.write(tags)




