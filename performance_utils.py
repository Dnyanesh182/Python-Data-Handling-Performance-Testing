"""
Performance benchmarking utilities for algorithm comparison.
Provides clean, reusable functions for measuring and comparing performance.
"""

import time
from typing import List, Callable, Dict, Any
from dataclasses import dataclass
from contextlib import contextmanager


@dataclass
class BenchmarkResult:
    """Container for benchmark results."""
    algorithm_name: str
    execution_time: float
    dataset_size: int
    result: Any = None
    
    def __str__(self) -> str:
        return (
            f"{self.algorithm_name}:\n"
            f"  Execution Time: {self.execution_time:.6f}s\n"
            f"  Dataset Size: {self.dataset_size:,}\n"
            f"  Result: {self.result}"
        )


class PerformanceTimer:
    """Context manager and utility for timing code execution."""
    
    def __init__(self):
        self.start_time: float = 0
        self.end_time: float = 0
        self.elapsed: float = 0
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time
        return False
    
    @staticmethod
    @contextmanager
    def measure():
        """
        Context manager for measuring execution time.
        
        Usage:
            with PerformanceTimer.measure() as timer:
                # code to measure
                pass
            print(f"Elapsed: {timer.elapsed}s")
        """
        timer = PerformanceTimer()
        timer.start_time = time.time()
        yield timer
        timer.end_time = time.time()
        timer.elapsed = timer.end_time - timer.start_time


class Benchmarker:
    """Utility for benchmarking algorithm performance."""
    
    @staticmethod
    def benchmark_function(
        func: Callable,
        *args,
        name: str = None,
        **kwargs
    ) -> BenchmarkResult:
        """
        Benchmark a single function execution.
        
        Args:
            func: Function to benchmark
            *args: Positional arguments for function
            name: Name for the benchmark (defaults to function name)
            **kwargs: Keyword arguments for function
            
        Returns:
            BenchmarkResult containing timing and result information
        """
        func_name = name or func.__name__
        dataset_size = len(args[0]) if args and hasattr(args[0], '__len__') else 0
        
        with PerformanceTimer.measure() as timer:
            result = func(*args, **kwargs)
        
        return BenchmarkResult(
            algorithm_name=func_name,
            execution_time=timer.elapsed,
            dataset_size=dataset_size,
            result=result
        )
    
    @staticmethod
    def compare_algorithms(
        algorithms: Dict[str, Callable],
        *args,
        **kwargs
    ) -> List[BenchmarkResult]:
        """
        Compare performance of multiple algorithms.
        
        Args:
            algorithms: Dictionary mapping names to algorithm functions
            *args: Positional arguments to pass to each algorithm
            **kwargs: Keyword arguments to pass to each algorithm
            
        Returns:
            List of BenchmarkResult objects, sorted by execution time
        """
        results = []
        
        for name, func in algorithms.items():
            # Create a copy of data for each algorithm to ensure fairness
            args_copy = tuple(
                arg.copy() if hasattr(arg, 'copy') else arg
                for arg in args
            )
            
            result = Benchmarker.benchmark_function(
                func,
                *args_copy,
                name=name,
                **kwargs
            )
            results.append(result)
        
        # Sort by execution time (fastest first)
        return sorted(results, key=lambda r: r.execution_time)
    
    @staticmethod
    def print_comparison(results: List[BenchmarkResult]) -> None:
        """
        Print formatted comparison of benchmark results.
        
        Args:
            results: List of BenchmarkResult objects
        """
        if not results:
            print("No results to display")
            return
        
        print("\n" + "=" * 60)
        print("PERFORMANCE COMPARISON RESULTS")
        print("=" * 60)
        
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result.algorithm_name}")
            print(f"   Time: {result.execution_time:.6f}s")
            print(f"   Dataset Size: {result.dataset_size:,}")
            
            if result.result is not None:
                print(f"   Result: {result.result}")
        
        # Calculate speedup
        if len(results) > 1:
            print("\n" + "-" * 60)
            print("SPEEDUP ANALYSIS")
            print("-" * 60)
            
            baseline = results[-1]  # Slowest algorithm
            fastest = results[0]    # Fastest algorithm
            
            for result in results:
                if result != baseline:
                    speedup = baseline.execution_time / result.execution_time
                    print(f"{result.algorithm_name} is {speedup:.2f}x faster than {baseline.algorithm_name}")
        
        print("=" * 60 + "\n")


class DatasetGenerator:
    """Utility for generating test datasets."""
    
    @staticmethod
    def generate_random_dataset(size: int, min_val: int = 1, max_val: int = 1000000) -> List[int]:
        """
        Generate random integer dataset.
        
        Args:
            size: Number of elements
            min_val: Minimum value
            max_val: Maximum value
            
        Returns:
            List of random integers
        """
        import random
        return [random.randint(min_val, max_val) for _ in range(size)]
    
    @staticmethod
    def generate_sorted_dataset(size: int, start: int = 0) -> List[int]:
        """
        Generate sorted integer dataset.
        
        Args:
            size: Number of elements
            start: Starting value
            
        Returns:
            List of sorted integers
        """
        return list(range(start, start + size))
    
    @staticmethod
    def generate_reverse_sorted_dataset(size: int, start: int = 0) -> List[int]:
        """
        Generate reverse-sorted integer dataset.
        
        Args:
            size: Number of elements
            start: Starting value
            
        Returns:
            List of reverse-sorted integers
        """
        return list(range(start + size - 1, start - 1, -1))
