# 🧠 AI Interview Simulator

## 🚀 Overview
An AI-powered interview preparation system that:
- Generates role-based questions
- Evaluates answers using NLP
- Provides keyword + similarity scoring

## 🧩 Features
- Question Generator (filtered by category/difficulty)
- Answer Evaluation (TF-IDF + Cosine Similarity)
- Keyword Gap Analysis
- LLM Feedback (optional)

## ⚙️ Tech Stack
- Python
- Streamlit
- Scikit-learn
- Transformers (optional)

## 📊 Demo
(Add screenshots here)

## 🏗️ Architecture
Explain pipeline:
Dataset → Question → User Answer → Evaluation → Feedback

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run src/streamlit_app.py
