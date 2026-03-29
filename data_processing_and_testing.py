# UC8 – Compare performance of algorithms using real dataset from CSV/JSON

from typing import List
import csv
import json
import time


class DataLoader:
    """Load data from CSV or JSON."""

    @staticmethod
    def load_csv(file_path: str) -> List[int]:
        data: List[int] = []
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        data.append(int(row.get("value", 0)))
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("CSV file not found.")
        return data

    @staticmethod
    def load_json(file_path: str) -> List[int]:
        data: List[int] = []
        try:
            with open(file_path, "r") as file:
                records = json.load(file)
                for item in records:
                    try:
                        data.append(int(item.get("value", 0)))
                    except (ValueError, AttributeError):
                        continue
        except FileNotFoundError:
            print("JSON file not found.")
        return data


class Algorithms:
    """Search algorithms for comparison."""

    @staticmethod
    def linear_search(data: List[int], target: int) -> int:
        for i, val in enumerate(data):
            if val == target:
                return i
        return -1

    @staticmethod
    def binary_search(data: List[int], target: int) -> int:
        data.sort()
        low, high = 0, len(data) - 1

        while low <= high:
            mid = (low + high) // 2
            if data[mid] == target:
                return mid
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


def compare(data: List[int]) -> None:
    """Compare algorithm performance."""
    if not data:
        print("No data available.")
        return

    target = data[-1]

    start = time.time()
    Algorithms.linear_search(data, target)
    linear_time = time.time() - start

    start = time.time()
    Algorithms.binary_search(data.copy(), target)
    binary_time = time.time() - start

    print(f"Dataset Size: {len(data)}")
    print(f"Linear Search Time: {linear_time:.6f}s")
    print(f"Binary Search Time: {binary_time:.6f}s")
    print("-" * 40)


def main() -> None:
    """Main execution function."""
    csv_data = DataLoader.load_csv("data.csv")
    json_data = DataLoader.load_json("data.json")

    print("CSV Data Performance:")
    compare(csv_data)

    print("JSON Data Performance:")
    compare(json_data)


if __name__ == "__main__":
    main()