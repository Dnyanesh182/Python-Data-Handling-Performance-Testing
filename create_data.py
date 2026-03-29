import csv
import json
import random

random.seed(42)
NUM_ROWS = 100000
MIN_VALUE = 1
MAX_VALUE = 1000000

print("Generating CSV...")
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["value"])
    writer.writeheader()
    for _ in range(NUM_ROWS):
        writer.writerow({"value": random.randint(MIN_VALUE, MAX_VALUE)})
print("CSV created!")

print("Generating JSON...")
data = [{"value": random.randint(MIN_VALUE, MAX_VALUE)} for _ in range(NUM_ROWS)]
with open("data.json", "w") as f:
    json.dump(data, f)
print("JSON created!")

print(f"\nFiles created with {NUM_ROWS:,} rows each")
