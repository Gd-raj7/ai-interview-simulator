from transformers import pipeline

class LLMFeedback:

    def __init__(self):
        # Load lightweight model
        self.generator = pipeline(
            "text-generation",
            model="distilgpt2"   # small, fast model
        )

    def generate_feedback(self, question, correct_answer, user_answer):

        prompt = f"""
You are an AI interview evaluator.

Question: {question}

Correct Answer: {correct_answer}

User Answer: {user_answer}

Give:
1. Strengths
2. Weaknesses
3. Suggestions
"""

        response = self.generator(
            prompt,
            max_length=200,
            num_return_sequences=1,
            temperature=0.7
        )

        return response[0]["generated_text"]