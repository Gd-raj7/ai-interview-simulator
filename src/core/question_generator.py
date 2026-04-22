import pandas as pd
import random

class QuestionGenerator:
    def __init__(self, dataset_path):
        self.df = pd.read_json(dataset_path)

    def get_random_question(self):
        return self.df.sample(1).iloc[0]

    def get_filtered_question(self, category=None, difficulty=None):
        filtered = self.df

        if category:
            filtered = filtered[filtered["category"] == category]

        if difficulty:
            filtered = filtered[filtered["difficulty"] == difficulty]

        if filtered.empty:
            raise ValueError("No questions found for given filters")

        return filtered.sample(1).iloc[0]