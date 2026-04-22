from core.keyword_extractor import KeywordExtractor

ke = KeywordExtractor()

text = "Overfitting occurs when a model learns noise instead of patterns"

keywords = ke.extract_keywords(text)

print("Keywords:", keywords)