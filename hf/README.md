# 🇫🇷 Legal AI Assistant (French) – LexisNexis Demo

> A multilingual legal clause retriever, classifier, and high-performance NER demo for French legal documents.

⚖️ Built for legal professionals to search, analyze, and classify clauses in French contracts using cutting-edge AI.

---

## 🧠 Features

- 🔍 **RAG-powered Document Search** (Retrieval-Augmented Generation)
- 🏷️ **Fine-Tuned French Legal NER** (`mBERT` trained with `accelerate`)
- 📚 **Clause Classification & Explanation**
- 🧾 **Downloadable Clause Output (PDF/Markdown)**
- 🧪 **Model Transparency Panel**

NER: Named Entity Recognition

---

## 🛠️ Tech Stack

- **Streamlit** – Frontend web app
- **Hugging Face Transformers** – LLM backbone
- **RAG + FAISS** – For fast legal clause retrieval
- **Accelerate** – Optimized training for fine-tuned French NER
- **Langchain** – Modular pipeline for prompt handling
- **Hugging Face Spaces + CI/CD** – For automated deployment




---

## 💡 How to Use

1. 📂 Upload or paste your legal document (in French)
2. 🧠 The model extracts and classifies clauses
3. 🏷️ Named Entities (e.g., parties, dates, obligations) are highlighted
4. 📤 You can **download the analysis**
5. 🧾 See **explanations** of what each AI component does

---

## 🧬 Model Explanation Panel

We include a collapsible sidebar that explains:
- How the NER model was fine-tuned
- What each clause label means
- How retrieval ranking works (e.g., with cross-encoders)

---

## 📥 Download Clauses Button

Click the **“📥 Download”** button to export selected clauses in:
- PDF
- Markdown
- Plain text

---

## 🚀 Accelerated Fine-Tuning

This project uses `accelerate` to train a **custom French NER model** on legal phrase spans.

Benefits:
- Mixed precision training (faster & lighter)
- Automatically detects hardware (GPU/CPU)
- Handles distributed training easily

---

## ⚙️ CI/CD & Deployment

This project is automatically:
- Deployed to **Hugging Face Spaces**
- Synced with **GitHub via GitHub Actions**
- Built using a `.huggingface.yaml` config

---

## 📎 Repository Structure

legal-ai-fr/
│
├── hf/ <- Streamlit app for Hugging Face Spaces
│ ├── app.py <- Main app
│ ├── requirements.txt <- Dependencies
│ ├── .huggingface.yaml <- Space config
│ ├── Dockerfile <- Optional for full control
│ ├── README.md <- You are here!
│ └── model/ <- Your fine-tuned NER model
│
├── accelerate_train_ner.py <- Local training script (not deployed)
├── ner_utils.py <- Helper functions for NER & tagging
└── .github/workflows/ <- GitHub Actions for CI/CD


---

## 🔒 Note on Confidentiality

This demo excludes unpublished models under review. Final versions will be shared after review. If you Are from **LexisNexis**, please reach out for a detailed walkthrough and confidential material access.

---

## 📢 Contact

Yashine Hazmatally Goolam Hossen  
📧 yashineonline@gmail.com  
📍 Waterloo, ON, Canada









# EXTRA

## ✅ What does accelerate do? 
accelerate is a tool from Hugging Face that helps you train machine learning models faster and more efficiently, especially on powerful hardware like GPUs or TPUs.
It automatically handles things like:

- Distributing training across multiple GPUs or machines

- Mixed precision (for faster training with less memory)

- Device placement (CPU, GPU, etc.)

- Logging and progress bars

It simplifies code that would normally be complex and hardware-specific.