import streamlit as st
from core.question_generator import QuestionGenerator
from core.answer_evaluator import AnswerEvaluator
from core.llm_feedback import LLMFeedback
import os

# -----------------------------
# Setup Paths
# -----------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(base_dir, "..", "data", "processed", "final_scoring_dataset.json")

# -----------------------------
# Initialize Components
# -----------------------------
qg = QuestionGenerator(dataset_path)
evaluator = AnswerEvaluator()
llm = LLMFeedback()

st.set_page_config(layout="wide")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🧠 InterviewAI")
st.sidebar.markdown("Executive Presence")

if st.sidebar.button("➕ New Session"):
    st.session_state.clear()
    st.rerun()

# -----------------------------
# Header
# -----------------------------
st.title("AI Interview Simulator")
st.caption("Practice and get AI-powered feedback")

# -----------------------------
# Settings
# -----------------------------
use_llm = st.checkbox("🤖 Enable AI Feedback (uses API)")

# -----------------------------
# Filters
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    category = st.text_input("Category")

with col2:
    difficulty = st.selectbox("Difficulty", ["", "easy", "medium", "hard"])

with col3:
    generate = st.button("✨ Generate Question")

# -----------------------------
# Generate Question
# -----------------------------
if generate:
    try:
        question = qg.get_filtered_question(
            category.lower() if category else None,
            difficulty if difficulty else None
        )
    except:
        question = qg.get_random_question()

    st.session_state["question"] = question

# -----------------------------
# Show Question
# -----------------------------
if "question" in st.session_state:
    st.markdown("### 📌 Current Prompt")
    st.info(st.session_state["question"]["question"])

    # -----------------------------
    # Answer Input
    # -----------------------------
    user_answer = st.text_area("✍️ Your Response", height=200)

    submit = st.button("🚀 Submit Answer")

    # -----------------------------
    # Evaluation
    # -----------------------------
    if submit:
        if not user_answer.strip():
            st.warning("Please enter your answer.")
        else:
            # -------- Rule-based evaluation --------
            result = evaluator.evaluate(
                st.session_state["question"]["answer"],
                user_answer
            )

            st.session_state["result"] = result
            st.session_state["user_answer"] = user_answer

# -----------------------------
# Show Results (persist after rerun)
# -----------------------------
if "result" in st.session_state:

    result = st.session_state["result"]

    st.markdown("## 📊 Evaluation Output")

    c1, c2, c3 = st.columns(3)

    c1.metric("Similarity", result["similarity"])
    c2.metric("Keyword Score", result["keyword_score"])
    c3.metric("Final Score", result["final_score"])

    # -----------------------------
    # Result Status
    # -----------------------------
    if result["final_score"] > 0.7:
        st.success("Strong Answer ✅")
    elif result["final_score"] > 0.4:
        st.warning("Needs Improvement ⚠️")
    else:
        st.error("Weak Answer ❌")

    # -----------------------------
    # Rule-Based Feedback
    # -----------------------------
    st.markdown("### 🔍 Keyword Feedback")

    st.write("🟢 Matched Keywords:", result["matched_keywords"])
    st.write("🔴 Missing Keywords:", result["missing_keywords"])

    if result["missing_keywords"]:
        st.info("💡 Improve by adding: " + ", ".join(result["missing_keywords"]))

    # -----------------------------
    # LLM Feedback (Optional)
    # -----------------------------
    if use_llm:
        if "llm_feedback" not in st.session_state:
            with st.spinner("🧠 AI analyzing your answer..."):
                try:
                    feedback = llm.generate_feedback(
                        st.session_state["question"]["question"],
                        st.session_state["question"]["answer"],
                        st.session_state["user_answer"]
                    )

                    st.session_state["llm_feedback"] = feedback

                except Exception as e:
                    st.error("LLM Error: " + str(e))

        # Show stored LLM result
        if "llm_feedback" in st.session_state:
            st.markdown("### 🤖 AI Feedback")
            st.write(st.session_state["llm_feedback"])