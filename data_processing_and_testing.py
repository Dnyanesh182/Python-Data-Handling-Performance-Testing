# UC9 – Implement unit testing for all use cases using pytest framework

from typing import List


class Algorithms:
    """Sample algorithms for testing."""

    @staticmethod
    def linear_search(data: List[int], target: int) -> int:
        for i, val in enumerate(data):
            if val == target:
                return i
        return -1

    @staticmethod
    def binary_search(data: List[int], target: int) -> int:
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


# ----------- Pytest Test Cases -----------

def test_linear_search_found():
    assert Algorithms.linear_search([1, 2, 3, 4], 3) == 2


def test_linear_search_not_found():
    assert Algorithms.linear_search([1, 2, 3, 4], 5) == -1


def test_binary_search_found():
    assert Algorithms.binary_search([1, 2, 3, 4, 5], 4) == 3


def test_binary_search_not_found():
    assert Algorithms.binary_search([1, 2, 3, 4, 5], 6) == -1


def test_empty_input():
    assert Algorithms.linear_search([], 1) == -1
    assert Algorithms.binary_search([], 1) == -1


def main() -> None:
    """Dummy main for execution."""
    print("Run 'pytest' command to execute test cases.")


if __name__ == "__main__":
    main()