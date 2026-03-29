# UC1 – Analyze time complexity of algorithms using practical input size benchmarking

from typing import List
import time


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


def benchmark(sizes: List[int]) -> None:
    """Benchmark algorithms with different input sizes."""
    print("Time Complexity Benchmarking:\n")

    for size in sizes:
        data = list(range(size))
        target = data[-1] if data else -1

        # Linear Search
        start = time.time()
        Algorithms.linear_search(data, target)
        linear_time = time.time() - start

        # Binary Search
        start = time.time()
        Algorithms.binary_search(data, target)
        binary_time = time.time() - start

        print(f"Input Size: {size}")
        print(f"Linear Search Time: {linear_time:.6f}s")
        print(f"Binary Search Time: {binary_time:.6f}s")
        print("-" * 40)


def main() -> None:
    """Main execution function."""
    sizes: List[int] = [10, 100, 1000, 10000]

    benchmark(sizes)


if __name__ == "__main__":
    main()