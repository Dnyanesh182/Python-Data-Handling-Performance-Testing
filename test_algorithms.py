"""
UC9 - Unit Testing using pytest for search algorithms
Tests for linear_search and binary_search with edge case coverage
"""

import pytest
from data_processing_and_testing import Algorithms


class TestLinearSearch:
    """Test cases for linear search algorithm."""
    
    def test_linear_search_found_first_element(self):
        """Test finding element at first position."""
        data = [1, 2, 3, 4, 5]
        assert Algorithms.linear_search(data, 1) == 0
    
    def test_linear_search_found_last_element(self):
        """Test finding element at last position."""
        data = [1, 2, 3, 4, 5]
        assert Algorithms.linear_search(data, 5) == 4
    
    def test_linear_search_found_middle_element(self):
        """Test finding element in middle position."""
        data = [1, 2, 3, 4, 5]
        assert Algorithms.linear_search(data, 3) == 2
    
    def test_linear_search_not_found(self):
        """Test searching for non-existent element."""
        data = [1, 2, 3, 4, 5]
        assert Algorithms.linear_search(data, 10) == -1
    
    def test_linear_search_empty_list(self):
        """Test searching in empty list."""
        data = []
        assert Algorithms.linear_search(data, 1) == -1
    
    def test_linear_search_single_element_found(self):
        """Test searching in single element list - found."""
        data = [42]
        assert Algorithms.linear_search(data, 42) == 0
    
    def test_linear_search_single_element_not_found(self):
        """Test searching in single element list - not found."""
        data = [42]
        assert Algorithms.linear_search(data, 10) == -1
    
    def test_linear_search_duplicate_values(self):
        """Test searching with duplicate values - returns first occurrence."""
        data = [1, 2, 3, 2, 5]
        assert Algorithms.linear_search(data, 2) == 1
    
    def test_linear_search_negative_numbers(self):
        """Test searching with negative numbers."""
        data = [-5, -3, -1, 0, 2, 4]
        assert Algorithms.linear_search(data, -3) == 1
    
    def test_linear_search_large_dataset(self):
        """Test searching in large dataset."""
        data = list(range(10000))
        assert Algorithms.linear_search(data, 9999) == 9999


class TestBinarySearch:
    """Test cases for binary search algorithm."""
    
    def test_binary_search_found_first_element(self):
        """Test finding element at first position."""
        data = [1, 2, 3, 4, 5]
        result = Algorithms.binary_search(data, 1)
        assert result != -1
        assert data[result] == 1
    
    def test_binary_search_found_last_element(self):
        """Test finding element at last position."""
        data = [1, 2, 3, 4, 5]
        result = Algorithms.binary_search(data, 5)
        assert result != -1
        assert data[result] == 5
    
    def test_binary_search_found_middle_element(self):
        """Test finding element in middle position."""
        data = [1, 2, 3, 4, 5]
        result = Algorithms.binary_search(data, 3)
        assert result != -1
        assert data[result] == 3
    
    def test_binary_search_not_found(self):
        """Test searching for non-existent element."""
        data = [1, 2, 3, 4, 5]
        assert Algorithms.binary_search(data, 10) == -1
    
    def test_binary_search_empty_list(self):
        """Test searching in empty list."""
        data = []
        assert Algorithms.binary_search(data, 1) == -1
    
    def test_binary_search_single_element_found(self):
        """Test searching in single element list - found."""
        data = [42]
        result = Algorithms.binary_search(data, 42)
        assert result != -1
        assert data[result] == 42
    
    def test_binary_search_single_element_not_found(self):
        """Test searching in single element list - not found."""
        data = [42]
        assert Algorithms.binary_search(data, 10) == -1
    
    def test_binary_search_unsorted_input(self):
        """Test binary search with unsorted input (algorithm sorts internally)."""
        data = [5, 2, 8, 1, 9]
        result = Algorithms.binary_search(data, 8)
        assert result != -1
        assert data[result] == 8
    
    def test_binary_search_duplicate_values(self):
        """Test searching with duplicate values."""
        data = [1, 2, 2, 2, 5]
        result = Algorithms.binary_search(data, 2)
        assert result != -1
        assert data[result] == 2
    
    def test_binary_search_negative_numbers(self):
        """Test searching with negative numbers."""
        data = [-5, -3, -1, 0, 2, 4]
        result = Algorithms.binary_search(data, -3)
        assert result != -1
        assert data[result] == -3
    
    def test_binary_search_large_dataset(self):
        """Test searching in large dataset."""
        data = list(range(10000))
        result = Algorithms.binary_search(data, 9999)
        assert result != -1
        assert data[result] == 9999
    
    def test_binary_search_target_smaller_than_all(self):
        """Test searching for value smaller than all elements."""
        data = [10, 20, 30, 40, 50]
        assert Algorithms.binary_search(data, 5) == -1
    
    def test_binary_search_target_larger_than_all(self):
        """Test searching for value larger than all elements."""
        data = [10, 20, 30, 40, 50]
        assert Algorithms.binary_search(data, 100) == -1


class TestEdgeCases:
    """Additional edge case tests."""
    
    def test_zero_value(self):
        """Test searching for zero."""
        data = [-2, -1, 0, 1, 2]
        assert Algorithms.linear_search(data, 0) == 2
        result = Algorithms.binary_search(data, 0)
        assert result != -1
        assert data[result] == 0
    
    def test_all_same_values(self):
        """Test list with all identical values."""
        data = [5, 5, 5, 5, 5]
        assert Algorithms.linear_search(data, 5) == 0
        result = Algorithms.binary_search(data, 5)
        assert result != -1
        assert data[result] == 5
    
    def test_two_elements(self):
        """Test list with exactly two elements."""
        data = [1, 2]
        assert Algorithms.linear_search(data, 1) == 0
        assert Algorithms.linear_search(data, 2) == 1
        
        result1 = Algorithms.binary_search(data, 1)
        assert result1 != -1
        assert data[result1] == 1
        
        result2 = Algorithms.binary_search(data, 2)
        assert result2 != -1
        assert data[result2] == 2


# Parametrized tests for comprehensive coverage
@pytest.mark.parametrize("data,target,expected_found", [
    ([1, 2, 3], 2, True),
    ([1, 2, 3], 4, False),
    ([100], 100, True),
    ([], 1, False),
    ([1, 1, 1], 1, True),
    ([-10, -5, 0, 5, 10], 0, True),
])
def test_linear_search_parametrized(data, target, expected_found):
    """Parametrized test for linear search."""
    result = Algorithms.linear_search(data, target)
    if expected_found:
        assert result != -1
    else:
        assert result == -1


@pytest.mark.parametrize("data,target,expected_found", [
    ([1, 2, 3], 2, True),
    ([1, 2, 3], 4, False),
    ([100], 100, True),
    ([], 1, False),
    ([1, 1, 1], 1, True),
    ([-10, -5, 0, 5, 10], 0, True),
])
def test_binary_search_parametrized(data, target, expected_found):
    """Parametrized test for binary search."""
    result = Algorithms.binary_search(data.copy(), target)
    if expected_found:
        assert result != -1
        assert data[result] == target
    else:
        assert result == -1
