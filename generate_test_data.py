"""Generate large CSV and JSON test datasets for performance testing."""

import csv
import json
import random

# Configuration
NUM_ROWS = 100000  # 100,000 rows for meaningful performance comparison
MIN_VALUE = 1
MAX_VALUE = 1000000

def generate_csv(filename: str = "data.csv", num_rows: int = NUM_ROWS) -> None:
    """Generate a large CSV file with random integer values."""
    print(f"Generating CSV file with {num_rows:,} rows...")
    
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["value"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for _ in range(num_rows):
            writer.writerow({"value": random.randint(MIN_VALUE, MAX_VALUE)})
    
    print(f"✓ CSV file '{filename}' created successfully!")


def generate_json(filename: str = "data.json", num_rows: int = NUM_ROWS) -> None:
    """Generate a large JSON file with random integer values."""
    print(f"Generating JSON file with {num_rows:,} rows...")
    
    data = []
    for _ in range(num_rows):
        data.append({"value": random.randint(MIN_VALUE, MAX_VALUE)})
    
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
    
    print(f"✓ JSON file '{filename}' created successfully!")


if __name__ == "__main__":
    print("=" * 50)
    print("Test Data Generator for Performance Testing")
    print("=" * 50)
    
    # Set seed for reproducibility
    random.seed(42)
    
    # Generate both files
    generate_csv("data.csv", NUM_ROWS)
    generate_json("data.json", NUM_ROWS)
    
    print("\n" + "=" * 50)
    print("Data generation complete!")
    print(f"Total rows per file: {NUM_ROWS:,}")
    print(f"Value range: {MIN_VALUE:,} to {MAX_VALUE:,}")
    print("=" * 50)
