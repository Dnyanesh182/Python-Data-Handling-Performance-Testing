"""
UC10 - Comprehensive unit tests for refactored modules.
Tests for file_utils, algorithms, performance_utils, and data_loader modules.
"""

import pytest
import tempfile
import json
import csv
from pathlib import Path
from file_utils import FileReader, FileWriter, DataConverter
from algorithms import SearchAlgorithms, SortAlgorithms, DataAnalyzer
from performance_utils import Benchmarker, PerformanceTimer, BenchmarkResult
from data_loader import DataLoader


# ==================== FILE_UTILS TESTS ====================

class TestFileReader:
    """Tests for FileReader class."""
    
    def test_read_csv_success(self, tmp_path):
        """Test successful CSV reading."""
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("name,age\nAlice,30\nBob,25")
        
        data = FileReader.read_csv(str(csv_file))
        assert len(data) == 2
        assert data[0]["name"] == "Alice"
        assert data[1]["age"] == "25"
    
    def test_read_csv_file_not_found(self):
        """Test CSV reading with non-existent file."""
        with pytest.raises(FileNotFoundError):
            FileReader.read_csv("nonexistent.csv")
    
    def test_read_json_success(self, tmp_path):
        """Test successful JSON reading."""
        json_file = tmp_path / "test.json"
        json_file.write_text('[{"name": "Alice", "age": 30}]')
        
        data = FileReader.read_json(str(json_file))
        assert len(data) == 1
        assert data[0]["name"] == "Alice"
    
    def test_read_json_file_not_found(self):
        """Test JSON reading with non-existent file."""
        with pytest.raises(FileNotFoundError):
            FileReader.read_json("nonexistent.json")


class TestFileWriter:
    """Tests for FileWriter class."""
    
    def test_write_csv(self, tmp_path):
        """Test CSV writing."""
        csv_file = tmp_path / "output.csv"
        data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        
        FileWriter.write_csv(str(csv_file), data)
        
        assert csv_file.exists()
        content = FileReader.read_csv(str(csv_file))
        assert len(content) == 2
    
    def test_write_json(self, tmp_path):
        """Test JSON writing."""
        json_file = tmp_path / "output.json"
        data = [{"name": "Alice", "age": 30}]
        
        FileWriter.write_json(str(json_file), data)
        
        assert json_file.exists()
        content = FileReader.read_json(str(json_file))
        assert len(content) == 1


class TestDataConverter:
    """Tests for DataConverter class."""
    
    def test_extract_column(self):
        """Test column extraction."""
        data = [{"value": "10"}, {"value": "20"}, {"value": "30"}]
        result = DataConverter.extract_column(data, "value", int)
        assert result == [10, 20, 30]
    
    def test_extract_column_with_missing_values(self):
        """Test column extraction with missing values."""
        data = [{"value": "10"}, {}, {"value": "30"}]
        result = DataConverter.extract_column(data, "value", int)
        assert result == [10, 30]


# ==================== ALGORITHMS TESTS ====================

class TestSearchAlgorithms:
    """Tests for SearchAlgorithms class."""
    
    def test_linear_search_found(self):
        """Test linear search - element found."""
        data = [1, 2, 3, 4, 5]
        assert SearchAlgorithms.linear_search(data, 3) == 2
    
    def test_linear_search_not_found(self):
        """Test linear search - element not found."""
        data = [1, 2, 3, 4, 5]
        assert SearchAlgorithms.linear_search(data, 10) == -1
    
    def test_binary_search_found(self):
        """Test binary search - element found."""
        data = [5, 2, 8, 1, 9]
        result = SearchAlgorithms.binary_search(data, 8)
        assert result != -1
    
    def test_binary_search_not_found(self):
        """Test binary search - element not found."""
        data = [1, 2, 3, 4, 5]
        assert SearchAlgorithms.binary_search(data, 10) == -1
    
    def test_binary_search_iterative(self):
        """Test iterative binary search."""
        data = [1, 2, 3, 4, 5]
        assert SearchAlgorithms.binary_search_iterative(data, 3) == 2
    
    def test_binary_search_recursive(self):
        """Test recursive binary search."""
        data = [1, 2, 3, 4, 5]
        assert SearchAlgorithms.binary_search_recursive(data, 3) == 2


class TestSortAlgorithms:
    """Tests for SortAlgorithms class."""
    
    def test_bubble_sort(self):
        """Test bubble sort."""
        data = [64, 34, 25, 12, 22, 11, 90]
        sorted_data = SortAlgorithms.bubble_sort(data)
        assert sorted_data == [11, 12, 22, 25, 34, 64, 90]
    
    def test_quick_sort(self):
        """Test quick sort."""
        data = [64, 34, 25, 12, 22, 11, 90]
        sorted_data = SortAlgorithms.quick_sort(data)
        assert sorted_data == [11, 12, 22, 25, 34, 64, 90]


class TestDataAnalyzer:
    """Tests for DataAnalyzer class."""
    
    def test_find_min_max(self):
        """Test finding min and max."""
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        min_val, max_val = DataAnalyzer.find_min_max(data)
        assert min_val == 1
        assert max_val == 9
    
    def test_calculate_average(self):
        """Test average calculation."""
        data = [1, 2, 3, 4, 5]
        assert DataAnalyzer.calculate_average(data) == 3.0
    
    def test_find_median_odd(self):
        """Test median with odd number of elements."""
        data = [1, 2, 3, 4, 5]
        assert DataAnalyzer.find_median(data) == 3.0
    
    def test_find_median_even(self):
        """Test median with even number of elements."""
        data = [1, 2, 3, 4]
        assert DataAnalyzer.find_median(data) == 2.5


# ==================== PERFORMANCE_UTILS TESTS ====================

class TestPerformanceTimer:
    """Tests for PerformanceTimer class."""
    
    def test_timer_context_manager(self):
        """Test timer as context manager."""
        with PerformanceTimer.measure() as timer:
            sum([i for i in range(1000)])
        
        assert timer.elapsed > 0
        assert timer.elapsed < 1  # Should be very fast


class TestBenchmarker:
    """Tests for Benchmarker class."""
    
    def test_benchmark_function(self):
        """Test single function benchmark."""
        data = list(range(100))
        result = Benchmarker.benchmark_function(
            SearchAlgorithms.linear_search,
            data,
            50,
            name="Linear Search Test"
        )
        
        assert isinstance(result, BenchmarkResult)
        assert result.algorithm_name == "Linear Search Test"
        assert result.execution_time > 0
        assert result.dataset_size == 100
    
    def test_compare_algorithms(self):
        """Test algorithm comparison."""
        data = list(range(100))
        algorithms = {
            "Linear": SearchAlgorithms.linear_search,
            "Binary": SearchAlgorithms.binary_search,
        }
        
        results = Benchmarker.compare_algorithms(algorithms, data, 50)
        
        assert len(results) == 2
        assert all(isinstance(r, BenchmarkResult) for r in results)


# ==================== DATA_LOADER TESTS ====================

class TestDataLoader:
    """Tests for DataLoader class."""
    
    def test_load_csv(self, tmp_path):
        """Test loading CSV data."""
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("value\n10\n20\n30")
        
        data = DataLoader.load_csv(str(csv_file))
        assert data == [10, 20, 30]
    
    def test_load_json(self, tmp_path):
        """Test loading JSON data."""
        json_file = tmp_path / "test.json"
        json_file.write_text('[{"value": 10}, {"value": 20}]')
        
        data = DataLoader.load_json(str(json_file))
        assert data == [10, 20]
    
    def test_load_from_multiple_sources(self, tmp_path):
        """Test loading from multiple files."""
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("value\n10\n20")
        
        json_file = tmp_path / "test.json"
        json_file.write_text('[{"value": 30}, {"value": 40}]')
        
        data = DataLoader.load_from_multiple_sources([
            str(csv_file),
            str(json_file)
        ])
        
        assert len(data) == 4
        assert 10 in data and 40 in data


# ==================== INTEGRATION TESTS ====================

class TestIntegration:
    """Integration tests combining multiple modules."""
    
    def test_full_workflow(self, tmp_path):
        """Test complete workflow from file to analysis."""
        # Create test data
        csv_file = tmp_path / "data.csv"
        test_data = [{"value": i} for i in range(1, 101)]
        FileWriter.write_csv(str(csv_file), test_data)
        
        # Load data
        loaded_data = DataLoader.load_csv(str(csv_file))
        
        # Analyze
        min_val, max_val = DataAnalyzer.find_min_max(loaded_data)
        avg = DataAnalyzer.calculate_average(loaded_data)
        
        # Assertions
        assert len(loaded_data) == 100
        assert min_val == 1
        assert max_val == 100
        assert avg == 50.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
