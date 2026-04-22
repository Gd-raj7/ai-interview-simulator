# TODO: Implement
from core.question_generator import QuestionGenerator
from core.answer_evaluator import AnswerEvaluator


def main():
    print("=== AI Interview Simulator ===\n")

    # Load components
    dataset_path = "../data/processed/final_scoring_dataset.json"
    qg = QuestionGenerator(dataset_path)
    evaluator = AnswerEvaluator()

    # -----------------------------
    # User Preferences
    # -----------------------------
    category = input("Enter category (machine learning / statistics / python) or press Enter: ").lower()
    difficulty = input("Enter difficulty (easy / medium / hard) or press Enter: ").lower()

    if category == "":
        category = None
    if difficulty == "":
        difficulty = None

    # -----------------------------
    # Get Question
    # -----------------------------
    try:
        question = qg.get_filtered_question(category, difficulty)
    except:
        print("\nNo matching question found → using random question.\n")
        question = qg.get_random_question()

    print("\n🧠 Question:")
    print(question["question"])

    # -----------------------------
    # User Answer
    # -----------------------------
    user_answer = input("\n✍️ Your Answer: ")

    # -----------------------------
    # Evaluate Answer
    # -----------------------------
    result = evaluator.evaluate(question["answer"], user_answer)

    # -----------------------------
    # Show Result
    # -----------------------------
    print("\n=== 📊 Evaluation Result ===")
    print("✅ Correct Answer:", question["answer"])
    print("📈 Similarity Score:", result["similarity"])
    print("🔑 Keyword Score:", result["keyword_score"])
    print("🏁 Final Score:", result["final_score"])
    print("🎯 Result:", result["result"])

    # -----------------------------
    # Feedback
    # -----------------------------
    print("\n🟢 Matched Keywords:", result["matched_keywords"])
    print("🔴 Missing Keywords:", result["missing_keywords"])

    if result["missing_keywords"]:
        print("\n💡 Suggestion: Try including concepts like:",
              ", ".join(result["missing_keywords"]))


if __name__ == "__main__":
    main()