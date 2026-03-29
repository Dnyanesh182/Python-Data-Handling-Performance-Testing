# UC6 – Write structured data into JSON file using serialization

from typing import List, Dict, Any
import json


class JSONWriter:
    """Class to handle JSON writing."""

    @staticmethod
    def write_json(file_path: str, data: List[Dict[str, Any]]) -> None:
        """
        Write structured data to JSON file.

        :param file_path: Output file path
        :param data: Data to serialize
        """
        if not data:
            print("No data to write.")
            return

        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)

            print(f"Data successfully written to {file_path}")

        except Exception as e:
            print(f"Error writing JSON: {e}")


def main() -> None:
    """Main execution function."""
    data: List[Dict[str, Any]] = [
        {"employee": {"name": "Alice", "salary": 50000}},
        {"employee": {"name": "Bob", "salary": 60000}},
    ]

    output_file = "output.json"

    JSONWriter.write_json(output_file, data)


if __name__ == "__main__":
    main()