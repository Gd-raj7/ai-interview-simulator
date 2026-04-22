# 🧠 AI Interview Simulator

🚀 **Live Demo:** http://ai-interview-simulator-ygbyjzhmna5jaushmo5mvy.streamlit.app/
📂 **GitHub Repo:** https://github.com/Gd-raj7/ai-interview-simulator

---

## 🚀 Overview

AI Interview Simulator is an end-to-end **AI-powered interview preparation system** that helps users practice technical and behavioral questions with real-time feedback.

It simulates a real interview environment by:

* Generating role-based questions
* Evaluating answers using NLP techniques
* Providing actionable feedback for improvement

---

## ✨ Features

* 🎯 **Dynamic Question Generator**

  * Filter by category and difficulty
  * Randomized interview prompts

* 🧠 **Answer Evaluation Engine**

  * TF-IDF vectorization
  * Cosine similarity scoring
  * Keyword matching

* 📊 **Performance Scoring**

  * Similarity score
  * Keyword coverage
  * Final evaluation score

* 💡 **Feedback System**

  * Missing keywords detection
  * Improvement suggestions

* 🌐 **Interactive UI**

  * Built with Streamlit
  * Clean and responsive layout

---

## 🏗️ System Architecture

```
Dataset (JSON)
     ↓
Question Generator
     ↓
User Input (Answer)
     ↓
Answer Evaluator
     ↓
Scores + Feedback
     ↓
Streamlit UI
```

---

## ⚙️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Data Processing:** Pandas
* **ML/NLP:** Scikit-learn (TF-IDF, Cosine Similarity)
* **Optional AI Layer:** Transformers (HuggingFace)

---

## ⚖️ Evaluation Logic

* **TF-IDF** → captures importance of words in answers
* **Cosine Similarity** → measures semantic closeness
* **Keyword Matching** → ensures concept coverage

### Limitation:

* Cannot fully understand deep context like advanced LLMs
* Works best for structured/technical answers

---

## ▶️ Run Locally

```bash
git clone https://github.com/Gd-raj7/ai-interview-simulator.git
cd ai-interview-simulator

pip install -r requirements.txt

streamlit run src/streamlit_app.py
```

---

## 📸 Screenshots

*Add your screenshots here (IMPORTANT for recruiters)*

* Question generation
* Answer input
* Evaluation output

---

## 🌐 Deployment

This project is deployed using Streamlit Cloud:

👉 http://ai-interview-simulator-ygbyjzhmna5jaushmo5mvy.streamlit.app/

---

## 📌 Future Improvements

* 🎙️ Voice-based interview mode
* 📄 Resume-based question generation
* 🤖 Advanced LLM feedback
* 📈 Performance analytics dashboard

---

## 🧠 Key Learning

* Built an end-to-end AI system (not just a model)
* Applied NLP techniques in a real-world scenario
* Designed modular and scalable architecture

---

## 📬 Contact

If you found this useful or want to collaborate:

* GitHub: https://github.com/Gd-raj7

---

⭐ If you like this project, consider giving it a star!
