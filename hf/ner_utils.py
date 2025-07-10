# ner_utils.py
#NER Model Loader & Inference
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

def load_ner_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForTokenClassification.from_pretrained(model_path)
    return model, tokenizer

def predict_ner(text, model, tokenizer):
    nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
    return nlp(text)




