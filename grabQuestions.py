import json
import random
import sqlparse

# Path to your Spider dataset JSON file
DATASET_PATH = "evaluation_examples/examples/train_spider.json"

def grab_random_questions(n, seed, addAnswers):
    random.seed(seed)
    print(f"Grabbing {n} random questions from the Spider dataset (seed={seed})")
    print()

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    samples = random.sample(data, n)
    for i, sample in enumerate(samples, 1):
        print(f"Question {i}: {sample['question']}")
        print(f"Database: {sample['db_id']}")
        
        if addAnswers:
            formatted_sql = sqlparse.format(sample['query'], reindent=True, keyword_case='upper')
            print()
            print("Answer:")
            print(formatted_sql)

        print()

if __name__ == "__main__":
    grab_random_questions(20, 10, True)