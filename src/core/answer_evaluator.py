# TODO: Implement
from unittest import result

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

from core.keyword_extractor import KeywordExtractor

class AnswerEvaluator:
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.ke = KeywordExtractor() 
    
    # -----------------------------
    # Text Cleaning
    # -----------------------------
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        return text
    
    # -----------------------------
    # Similarity Score
    # -----------------------------
    def compute_similarity(self, correct, user):
        texts = [correct, user]
        vectors = self.vectorizer.fit_transform(texts)
        score = cosine_similarity(vectors[0], vectors[1])[0][0]
        return score
    
    # -----------------------------
    # Keyword Matching
    # -----------------------------
    def keyword_match(self, correct, user):
        correct_words = set(correct.split())
        user_words = set(user.split())
        
        common = correct_words.intersection(user_words)
        
        if len(correct_words) == 0:
            return 0
        
        return len(common) / len(correct_words)
    
    # -----------------------------
    # Final Evaluation
    # -----------------------------
    def evaluate(self, correct_answer, user_answer):

    # Clean text
        correct = self.clean_text(correct_answer)
        user = self.clean_text(user_answer)

        # -----------------------------
        # Similarity
        # -----------------------------
        similarity = self.compute_similarity(correct, user)

        # -----------------------------
        # Keyword Extraction
        # -----------------------------
        correct_keywords = set(self.ke.extract_keywords(correct))
        user_keywords = set(self.ke.extract_keywords(user))

        matched = correct_keywords.intersection(user_keywords)
        missing = correct_keywords - user_keywords

        # Keyword score
        if len(correct_keywords) == 0:
            keyword_score = 0
        else:
            keyword_score = len(matched) / len(correct_keywords)

        # -----------------------------
        # Final Score
        # -----------------------------
        final_score = (0.6 * similarity) + (0.4 * keyword_score)

        # -----------------------------
        # Result Decision
        # -----------------------------
        if final_score > 0.7:
            result = "Correct"
        elif final_score > 0.4:
            result = "Partially Correct"
        else:
            result = "Incorrect"

        # -----------------------------
        # Return Output
        # -----------------------------
        return {
            "similarity": round(similarity, 2),
            "keyword_score": round(keyword_score, 2),
            "final_score": round(final_score, 2),
            "result": result,
            "matched_keywords": list(matched),
            "missing_keywords": list(missing)
        }
        