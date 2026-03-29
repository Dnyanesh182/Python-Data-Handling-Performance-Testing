"""
File utility module for handling CSV and JSON file operations.
Provides clean, reusable functions for data loading and saving.
"""

from typing import List, Dict, Any, Optional
import csv
import json
from pathlib import Path


class FileReader:
    """Handles reading operations for various file formats."""

    @staticmethod
    def read_csv(file_path: str, encoding: str = 'utf-8') -> List[Dict[str, str]]:
        """
        Read CSV file and return list of dictionaries.
        
        Args:
            file_path: Path to CSV file
            encoding: File encoding (default: utf-8)
            
        Returns:
            List of dictionaries representing CSV rows
            
        Raises:
            FileNotFoundError: If file doesn't exist
            csv.Error: If CSV parsing fails
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        
        try:
            with open(path, mode='r', encoding=encoding, newline='') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except csv.Error as e:
            raise csv.Error(f"Error parsing CSV file: {e}")

    @staticmethod
    def read_json(file_path: str, encoding: str = 'utf-8') -> List[Dict[str, Any]]:
        """
        Read JSON file and return parsed data.
        
        Args:
            file_path: Path to JSON file
            encoding: File encoding (default: utf-8)
            
        Returns:
            Parsed JSON data as list of dictionaries
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If JSON parsing fails
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"JSON file not found: {file_path}")
        
        try:
            with open(path, mode='r', encoding=encoding) as file:
                data = json.load(file)
                return data if isinstance(data, list) else [data]
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error parsing JSON file: {e.msg}", e.doc, e.pos)


class FileWriter:
    """Handles writing operations for various file formats."""

    @staticmethod
    def write_csv(
        file_path: str,
        data: List[Dict[str, Any]],
        fieldnames: Optional[List[str]] = None,
        encoding: str = 'utf-8'
    ) -> None:
        """
        Write data to CSV file.
        
        Args:
            file_path: Path to output CSV file
            data: List of dictionaries to write
            fieldnames: Column names (auto-detected if None)
            encoding: File encoding (default: utf-8)
        """
        if not data:
            raise ValueError("Cannot write empty data to CSV")
        
        if fieldnames is None:
            fieldnames = list(data[0].keys())
        
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, mode='w', encoding=encoding, newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def write_json(
        file_path: str,
        data: Any,
        indent: int = 2,
        encoding: str = 'utf-8'
    ) -> None:
        """
        Write data to JSON file.
        
        Args:
            file_path: Path to output JSON file
            data: Data to serialize to JSON
            indent: JSON indentation (default: 2)
            encoding: File encoding (default: utf-8)
        """
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, mode='w', encoding=encoding) as file:
            json.dump(data, file, indent=indent)


class DataConverter:
    """Utility for converting data between different formats."""

    @staticmethod
    def extract_column(data: List[Dict[str, Any]], column_name: str, data_type: type = str) -> List[Any]:
        """
        Extract a single column from list of dictionaries.
        
        Args:
            data: List of dictionaries
            column_name: Name of column to extract
            data_type: Type to convert values to (default: str)
            
        Returns:
            List of values from specified column
        """
        result = []
        for row in data:
            value = row.get(column_name)
            if value is not None:
                try:
                    result.append(data_type(value))
                except (ValueError, TypeError):
                    continue
        return result

    @staticmethod
    def csv_to_json(csv_path: str, json_path: str) -> None:
        """
        Convert CSV file to JSON format.
        
        Args:
            csv_path: Path to input CSV file
            json_path: Path to output JSON file
        """
        data = FileReader.read_csv(csv_path)
        FileWriter.write_json(json_path, data)

    @staticmethod
    def json_to_csv(json_path: str, csv_path: str, fieldnames: Optional[List[str]] = None) -> None:
        """
        Convert JSON file to CSV format.
        
        Args:
            json_path: Path to input JSON file
            csv_path: Path to output CSV file
            fieldnames: Column names for CSV (auto-detected if None)
        """
        data = FileReader.read_json(json_path)
        FileWriter.write_csv(csv_path, data, fieldnames)
