# TODO: Implement
from core.answer_evaluator import AnswerEvaluator

evaluator = AnswerEvaluator()

correct = "overfitting occurs when a model learns noise instead of patterns"
user = input("Your Answer: ")

result = evaluator.evaluate(correct, user)

print("\nEvaluation:")
print(result)