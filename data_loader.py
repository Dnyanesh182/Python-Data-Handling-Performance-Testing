"""
Data loading utilities specific to the performance testing application.
Integrates file_utils with algorithms for seamless data processing.
"""

from typing import List
from file_utils import FileReader, DataConverter


class DataLoader:
    """Handles loading and parsing data from various file formats."""

    @staticmethod
    def load_csv(file_path: str, column_name: str = "value") -> List[int]:
        """
        Load integer data from CSV file.
        
        Args:
            file_path: Path to CSV file
            column_name: Name of column containing values (default: "value")
            
        Returns:
            List of integers from specified column
        """
        try:
            csv_data = FileReader.read_csv(file_path)
            return DataConverter.extract_column(csv_data, column_name, int)
        except FileNotFoundError:
            print(f"Error: CSV file '{file_path}' not found.")
            return []
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return []

    @staticmethod
    def load_json(file_path: str, key: str = "value") -> List[int]:
        """
        Load integer data from JSON file.
        
        Args:
            file_path: Path to JSON file
            key: Key containing values in each JSON object (default: "value")
            
        Returns:
            List of integers from specified key
        """
        try:
            json_data = FileReader.read_json(file_path)
            return DataConverter.extract_column(json_data, key, int)
        except FileNotFoundError:
            print(f"Error: JSON file '{file_path}' not found.")
            return []
        except Exception as e:
            print(f"Error loading JSON: {e}")
            return []

    @staticmethod
    def load_from_multiple_sources(file_paths: List[str]) -> List[int]:
        """
        Load and combine data from multiple files (CSV or JSON).
        
        Args:
            file_paths: List of file paths to load
            
        Returns:
            Combined list of integers from all files
        """
        combined_data = []
        
        for path in file_paths:
            if path.endswith('.csv'):
                data = DataLoader.load_csv(path)
            elif path.endswith('.json'):
                data = DataLoader.load_json(path)
            else:
                print(f"Unsupported file format: {path}")
                continue
            
            combined_data.extend(data)
        
        return combined_data
