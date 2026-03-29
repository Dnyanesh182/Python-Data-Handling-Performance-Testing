# UC2 – Analyze space complexity by measuring memory usage during execution

from typing import List
import sys


class Algorithms:
    """Class containing sample algorithms."""

    @staticmethod
    def linear_search(data: List[int], target: int) -> int:
        for i, value in enumerate(data):
            if value == target:
                return i
        return -1

    @staticmethod
    def binary_search(data: List[int], target: int) -> int:
        low = 0
        high = len(data) - 1

        while low <= high:
            mid = (low + high) // 2
            if data[mid] == target:
                return mid
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


def analyze_space(sizes: List[int]) -> None:
    """Analyze memory usage for algorithms."""
    print("Space Complexity Analysis:\n")

    for size in sizes:
        data = list(range(size))
        target = data[-1] if data else -1

        # Memory usage of input data
        input_memory = sys.getsizeof(data)

        # Run algorithms (no significant extra space)
        Algorithms.linear_search(data, target)
        Algorithms.binary_search(data, target)

        print(f"Input Size: {size}")
        print(f"Memory Used by Data: {input_memory} bytes")
        print("-" * 40)


def main() -> None:
    """Main execution function."""
    sizes: List[int] = [10, 100, 1000, 10000]

    analyze_space(sizes)


if __name__ == "__main__":
    main()