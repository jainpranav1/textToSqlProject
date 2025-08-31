import json
import random

# Path to your Spider dataset JSON file
DATASET_PATH = "evaluation_examples/examples/train_spider.json"

def grab_random_questions(n):
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    samples = random.sample(data, n)
    for i, sample in enumerate(samples, 1):
        print(f"Question {i}: {sample['question']}")
        print(f"Database: {sample['db_id']}")
        print(f"SQL: {sample['query']}\n")

if __name__ == "__main__":
    grab_random_questions(10)