# TODO: Implement
import re

class KeywordExtractor:

    def __init__(self):
        # Common useless words
        self.stopwords = {
            "is", "a", "the", "and", "or", "in", "on", "at",
            "of", "to", "for", "with", "by", "an", "be",
            "this", "that", "it", "as", "are", "was"
        }

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        return text

    def extract_keywords(self, text):
        text = self.clean_text(text)
        words = text.split()

        # Remove stopwords
        keywords = [word for word in words if word not in self.stopwords]

        return keywords