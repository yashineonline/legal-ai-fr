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


'''
st.markdown("Upload a French legal document and extract entities (NER).")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("Document Preview", text[:1000], height=200)

    with st.spinner("Loading model..."):
        model_name = "Jean-Baptiste/roberta-large-ner-english"  # placeholder
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForTokenClassification.from_pretrained(model_name)
        ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

    with st.spinner("Extracting entities..."):
        results = ner_pipeline(text)
        for entity in results:
            st.markdown(f"- **{entity['entity_group']}**: `{entity['word']}` (score: {entity['score']:.2f})")
            '''

if query:
    st.subheader("📌 RAG Answer")
    rag_pipe = pipeline("text2text-generation", model="philschmid/bart-large-cnn-samsum")  # Placeholder RAG
    rag_response = rag_pipe(query, max_length=200, do_sample=False)[0]['generated_text']
    st.success(rag_response)

    st.subheader("📑 NER Clause Tagging")
    ner_model, tokenizer = load_ner_model("models/french_ner_model")
    tags = predict_ner(query, ner_model, tokenizer)
    st.write(tags)




