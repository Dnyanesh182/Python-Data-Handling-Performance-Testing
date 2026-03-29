"""
Algorithm implementations for searching and sorting.
Provides clean, reusable algorithm functions with proper documentation.
"""

from typing import List, Optional, Tuple


class SearchAlgorithms:
    """Collection of search algorithm implementations."""

    @staticmethod
    def linear_search(data: List[int], target: int) -> int:
        """
        Perform linear search to find target in data.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            data: List of integers to search
            target: Value to find
            
        Returns:
            Index of target if found, -1 otherwise
        """
        for index, value in enumerate(data):
            if value == target:
                return index
        return -1

    @staticmethod
    def binary_search(data: List[int], target: int) -> int:
        """
        Perform binary search to find target in data.
        Note: This implementation sorts the data internally.
        
        Time Complexity: O(n log n) due to sorting, O(log n) for search
        Space Complexity: O(1)
        
        Args:
            data: List of integers to search
            target: Value to find
            
        Returns:
            Index of target in sorted array if found, -1 otherwise
        """
        if not data:
            return -1
        
        # Sort the data (modifies in place)
        data.sort()
        
        low, high = 0, len(data) - 1
        
        while low <= high:
            mid = (low + high) // 2
            mid_value = data[mid]
            
            if mid_value == target:
                return mid
            elif target < mid_value:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1

    @staticmethod
    def binary_search_iterative(sorted_data: List[int], target: int) -> int:
        """
        Perform binary search on pre-sorted data (iterative approach).
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            sorted_data: Sorted list of integers
            target: Value to find
            
        Returns:
            Index of target if found, -1 otherwise
        """
        low, high = 0, len(sorted_data) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if sorted_data[mid] == target:
                return mid
            elif sorted_data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

    @staticmethod
    def binary_search_recursive(
        sorted_data: List[int],
        target: int,
        low: Optional[int] = None,
        high: Optional[int] = None
    ) -> int:
        """
        Perform binary search on pre-sorted data (recursive approach).
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) due to recursion stack
        
        Args:
            sorted_data: Sorted list of integers
            target: Value to find
            low: Lower bound index (defaults to 0)
            high: Upper bound index (defaults to len-1)
            
        Returns:
            Index of target if found, -1 otherwise
        """
        if low is None:
            low = 0
        if high is None:
            high = len(sorted_data) - 1
        
        if low > high:
            return -1
        
        mid = low + (high - low) // 2
        
        if sorted_data[mid] == target:
            return mid
        elif sorted_data[mid] < target:
            return SearchAlgorithms.binary_search_recursive(sorted_data, target, mid + 1, high)
        else:
            return SearchAlgorithms.binary_search_recursive(sorted_data, target, low, mid - 1)


class SortAlgorithms:
    """Collection of sorting algorithm implementations."""

    @staticmethod
    def bubble_sort(data: List[int]) -> List[int]:
        """
        Sort data using bubble sort algorithm.
        
        Time Complexity: O(n²)
        Space Complexity: O(1)
        
        Args:
            data: List of integers to sort
            
        Returns:
            Sorted list
        """
        arr = data.copy()
        n = len(arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            if not swapped:
                break
        
        return arr

    @staticmethod
    def quick_sort(data: List[int]) -> List[int]:
        """
        Sort data using quick sort algorithm.
        
        Time Complexity: O(n log n) average, O(n²) worst case
        Space Complexity: O(log n)
        
        Args:
            data: List of integers to sort
            
        Returns:
            Sorted list
        """
        if len(data) <= 1:
            return data
        
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        
        return SortAlgorithms.quick_sort(left) + middle + SortAlgorithms.quick_sort(right)


class DataAnalyzer:
    """Utility functions for data analysis."""

    @staticmethod
    def find_min_max(data: List[int]) -> Tuple[int, int]:
        """
        Find minimum and maximum values in data.
        
        Args:
            data: List of integers
            
        Returns:
            Tuple of (min, max)
            
        Raises:
            ValueError: If data is empty
        """
        if not data:
            raise ValueError("Cannot find min/max of empty list")
        
        return min(data), max(data)

    @staticmethod
    def calculate_average(data: List[int]) -> float:
        """
        Calculate average of data.
        
        Args:
            data: List of integers
            
        Returns:
            Average value
            
        Raises:
            ValueError: If data is empty
        """
        if not data:
            raise ValueError("Cannot calculate average of empty list")
        
        return sum(data) / len(data)

    @staticmethod
    def find_median(data: List[int]) -> float:
        """
        Find median value in data.
        
        Args:
            data: List of integers
            
        Returns:
            Median value
            
        Raises:
            ValueError: If data is empty
        """
        if not data:
            raise ValueError("Cannot find median of empty list")
        
        sorted_data = sorted(data)
        n = len(sorted_data)
        
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return float(sorted_data[n // 2])
