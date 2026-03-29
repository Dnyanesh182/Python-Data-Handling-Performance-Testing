# Python Data Handling & Performance Testing

A comprehensive Python project demonstrating data processing, algorithm performance comparison, and clean code architecture with reusable utility modules.

## 📁 Project Structure

```
Python-Data-Handling-Performance-Testing/
│
├── 📄 data_processing_and_testing.py  # Main application entry point
├── 📄 file_utils.py                   # File I/O operations (CSV, JSON)
├── 📄 algorithms.py                   # Search/sort algorithms
├── 📄 performance_utils.py            # Benchmarking utilities
├── 📄 data_loader.py                  # Application-specific data loading
│
├── 📄 test_algorithms.py              # UC9: Unit tests for algorithms
├── 📄 test_refactored_modules.py      # UC10: Tests for refactored modules
│
├── 📄 create_data.py                  # Generate test datasets
├── 📄 generate_test_data.py           # Alternative data generator
├── 📄 generate.bat                    # Batch script for data generation
│
└── 📄 README.md                       # This file
```

## 🎯 Features

### UC8: Performance Comparison
- Compare algorithm performance using real datasets (CSV/JSON)
- Support for large datasets (100,000+ records)
- Detailed timing and speedup analysis

### UC9: Unit Testing
- Comprehensive pytest test suite
- Edge case coverage
- Parametrized tests for thorough validation

### UC10: Clean Code Refactoring
- **Modular architecture** following SOLID principles
- **Reusable utility modules** for file handling, algorithms, and performance testing
- **Proper error handling** and documentation
- **Type hints** for better code clarity

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install pytest
```

### 2. Generate Test Data

```bash
python create_data.py
```

This creates:
- `data.csv` - 100,000 rows with random integer values
- `data.json` - Same data in JSON format

### 3. Run Main Application

```bash
python data_processing_and_testing.py
```

### 4. Run Tests

```bash
# Run algorithm tests (UC9)
pytest test_algorithms.py -v

# Run refactored module tests (UC10)
pytest test_refactored_modules.py -v

# Run all tests
pytest -v
```

## 📦 Module Documentation

### `file_utils.py`
Provides clean file I/O operations:
- **FileReader**: Read CSV and JSON files with error handling
- **FileWriter**: Write data to CSV and JSON formats
- **DataConverter**: Convert between formats and extract columns

### `algorithms.py`
Implements search and sort algorithms:
- **SearchAlgorithms**: Linear search, binary search (iterative & recursive)
- **SortAlgorithms**: Bubble sort, quick sort
- **DataAnalyzer**: Min/max, average, median calculations

### `performance_utils.py`
Performance benchmarking tools:
- **PerformanceTimer**: Context manager for timing code execution
- **Benchmarker**: Compare multiple algorithms with detailed metrics
- **DatasetGenerator**: Generate test datasets for benchmarking

### `data_loader.py`
Application-specific data loading:
- Load integer data from CSV/JSON files
- Extract specific columns
- Combine data from multiple sources

## 🧪 Testing

The project includes two comprehensive test suites:

### `test_algorithms.py` (UC9)
- 30+ test cases for search algorithms
- Edge cases: empty lists, single elements, duplicates
- Parametrized tests for comprehensive coverage

### `test_refactored_modules.py` (UC10)
- Tests for all refactored modules
- Unit tests and integration tests
- File I/O, algorithms, performance utilities, data loading

## 📊 Example Usage

```python
from data_loader import DataLoader
from algorithms import SearchAlgorithms
from performance_utils import Benchmarker

# Load data
data = DataLoader.load_csv("data.csv")

# Compare algorithms
algorithms = {
    "Linear Search": SearchAlgorithms.linear_search,
    "Binary Search": SearchAlgorithms.binary_search,
}

results = Benchmarker.compare_algorithms(algorithms, data, target=5000)
Benchmarker.print_comparison(results)
```

## 🎓 Learning Objectives

This project demonstrates:
- ✅ Clean code principles (SOLID, DRY, separation of concerns)
- ✅ Modular architecture and reusable utilities
- ✅ Comprehensive testing with pytest
- ✅ Performance benchmarking and analysis
- ✅ File I/O with proper error handling
- ✅ Type hints and documentation
- ✅ Algorithm implementation and comparison

## 📝 License

This project is for educational purposes.

---

**Author**: Python Data Handling & Performance Testing Project
**Version**: 2.0 (Refactored)
Comprehensive Python implementation covering algorithm performance analysis, CSV &amp; JSON data handling (including nested structures), and unit testing using pytest, following clean code and reusable module design principles.
