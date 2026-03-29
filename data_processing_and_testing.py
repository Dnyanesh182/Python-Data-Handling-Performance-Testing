# UC4 – Write processed data into CSV file with proper formatting

from typing import List, Dict
import csv


class CSVWriter:
    """Class to handle writing data to CSV."""

    @staticmethod
    def write_csv(file_path: str, data: List[Dict[str, str]]) -> None:
        """
        Write list of dictionaries to CSV file.

        :param file_path: Output CSV file path
        :param data: List of records
        """
        if not data:
            print("No data to write.")
            return

        try:
            fieldnames = data[0].keys()

            with open(file_path, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data)

            print(f"Data successfully written to {file_path}")

        except Exception as e:
            print(f"Error writing to CSV: {e}")


def main() -> None:
    """Main execution function."""
    data: List[Dict[str, str]] = [
        {"name": "Alice", "salary": "50000"},
        {"name": "Bob", "salary": "60000"},
    ]

    output_file = "output.csv"

    CSVWriter.write_csv(output_file, data)


if __name__ == "__main__":
    main()