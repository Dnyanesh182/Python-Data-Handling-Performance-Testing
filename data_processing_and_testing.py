# UC5 – Read JSON file and parse nested data structures

from typing import List, Dict, Any
import json


class JSONProcessor:
    """Class to handle JSON reading and parsing."""

    @staticmethod
    def read_json(file_path: str) -> List[Dict[str, Any]]:
        """
        Read JSON file and return data.

        :param file_path: Path to JSON file
        :return: Parsed JSON data
        """
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON format.")

        return []

    @staticmethod
    def extract_names(data: List[Dict[str, Any]]) -> List[str]:
        """Extract names from nested JSON structure."""
        names: List[str] = []

        for item in data:
            try:
                names.append(item["employee"]["name"])
            except KeyError:
                continue

        return names


def main() -> None:
    """Main execution function."""
    file_path = "employees.json"

    data = JSONProcessor.read_json(file_path)

    print("Raw Data:", data)

    names = JSONProcessor.extract_names(data)

    print("Extracted Names:", names)


if __name__ == "__main__":
    main()