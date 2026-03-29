"""
Demonstration script showing all features of the refactored modules.
Run this to see the clean architecture in action!
"""

from file_utils import FileReader, FileWriter, DataConverter
from algorithms import SearchAlgorithms, SortAlgorithms, DataAnalyzer
from performance_utils import Benchmarker, PerformanceTimer, DatasetGenerator
from data_loader import DataLoader


def demo_file_operations():
    """Demonstrate file I/O operations."""
    print("\n" + "=" * 70)
    print("DEMO 1: FILE OPERATIONS")
    print("=" * 70)
    
    # Create sample data
    sample_data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 87},
        {"id": 3, "name": "Charlie", "score": 92}
    ]
    
    print("\n📝 Writing data to files...")
    FileWriter.write_csv("demo_output.csv", sample_data)
    FileWriter.write_json("demo_output.json", sample_data)
    print("✓ Files created: demo_output.csv, demo_output.json")
    
    print("\n📖 Reading data back...")
    csv_data = FileReader.read_csv("demo_output.csv")
    json_data = FileReader.read_json("demo_output.json")
    print(f"✓ CSV records: {len(csv_data)}")
    print(f"✓ JSON records: {len(json_data)}")
    
    print("\n🔄 Extracting specific column...")
    scores = DataConverter.extract_column(csv_data, "score", int)
    print(f"✓ Scores: {scores}")


def demo_algorithms():
    """Demonstrate algorithm implementations."""
    print("\n" + "=" * 70)
    print("DEMO 2: ALGORITHMS")
    print("=" * 70)
    
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal data: {data}")
    
    # Search
    print("\n🔍 SEARCH OPERATIONS:")
    target = 25
    linear_result = SearchAlgorithms.linear_search(data, target)
    print(f"Linear search for {target}: index {linear_result}")
    
    binary_result = SearchAlgorithms.binary_search(data.copy(), target)
    print(f"Binary search for {target}: index {binary_result}")
    
    # Sort
    print("\n📊 SORTING OPERATIONS:")
    bubble_sorted = SortAlgorithms.bubble_sort(data)
    quick_sorted = SortAlgorithms.quick_sort(data)
    print(f"Bubble sort result: {bubble_sorted}")
    print(f"Quick sort result:  {quick_sorted}")
    
    # Analysis
    print("\n📈 DATA ANALYSIS:")
    min_val, max_val = DataAnalyzer.find_min_max(data)
    avg = DataAnalyzer.calculate_average(data)
    median = DataAnalyzer.find_median(data)
    print(f"Min: {min_val}, Max: {max_val}")
    print(f"Average: {avg:.2f}")
    print(f"Median: {median}")


def demo_performance_benchmarking():
    """Demonstrate performance benchmarking."""
    print("\n" + "=" * 70)
    print("DEMO 3: PERFORMANCE BENCHMARKING")
    print("=" * 70)
    
    # Generate test data
    print("\n📊 Generating test dataset...")
    data = DatasetGenerator.generate_random_dataset(10000)
    target = data[len(data) // 2]
    print(f"✓ Created dataset with {len(data):,} elements")
    
    # Benchmark individual function
    print("\n⏱️  Benchmarking linear search...")
    result = Benchmarker.benchmark_function(
        SearchAlgorithms.linear_search,
        data,
        target,
        name="Linear Search"
    )
    print(result)
    
    # Compare multiple algorithms
    print("\n⚡ Comparing search algorithms...")
    algorithms = {
        "Linear Search": SearchAlgorithms.linear_search,
        "Binary Search": SearchAlgorithms.binary_search,
    }
    results = Benchmarker.compare_algorithms(algorithms, data, target)
    Benchmarker.print_comparison(results)


def demo_integrated_workflow():
    """Demonstrate complete integrated workflow."""
    print("\n" + "=" * 70)
    print("DEMO 4: INTEGRATED WORKFLOW")
    print("=" * 70)
    
    print("\n🔄 Complete workflow: Generate → Save → Load → Process → Analyze")
    
    # Step 1: Generate data
    print("\n1️⃣  Generating dataset...")
    data = DatasetGenerator.generate_random_dataset(1000, 1, 100)
    print(f"   ✓ Generated {len(data):,} random integers")
    
    # Step 2: Save to file
    print("\n2️⃣  Saving to CSV...")
    formatted_data = [{"value": val} for val in data]
    FileWriter.write_csv("workflow_demo.csv", formatted_data)
    print("   ✓ Saved to workflow_demo.csv")
    
    # Step 3: Load from file
    print("\n3️⃣  Loading from CSV...")
    loaded_data = DataLoader.load_csv("workflow_demo.csv")
    print(f"   ✓ Loaded {len(loaded_data):,} values")
    
    # Step 4: Process data
    print("\n4️⃣  Processing data...")
    sorted_data = SortAlgorithms.quick_sort(loaded_data)
    print(f"   ✓ Sorted data: First 5 = {sorted_data[:5]}")
    
    # Step 5: Analyze
    print("\n5️⃣  Analyzing results...")
    min_val, max_val = DataAnalyzer.find_min_max(loaded_data)
    avg = DataAnalyzer.calculate_average(loaded_data)
    median = DataAnalyzer.find_median(loaded_data)
    print(f"   ✓ Statistics:")
    print(f"     - Range: {min_val} to {max_val}")
    print(f"     - Average: {avg:.2f}")
    print(f"     - Median: {median}")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 70)
    print("REFACTORED MODULE DEMONSTRATION")
    print("UC10: Clean Code & Reusable Utility Modules")
    print("=" * 70)
    
    try:
        demo_file_operations()
        demo_algorithms()
        demo_performance_benchmarking()
        demo_integrated_workflow()
        
        print("\n" + "=" * 70)
        print("✅ ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        print("\nRefactored modules provide:")
        print("  ✓ Clean, maintainable code structure")
        print("  ✓ Reusable utility functions")
        print("  ✓ Proper error handling")
        print("  ✓ Comprehensive documentation")
        print("  ✓ Type hints for better IDE support")
        print("  ✓ Performance benchmarking tools")
        print("=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
