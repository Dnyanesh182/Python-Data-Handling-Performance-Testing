# UC3 – Read data from CSV file and process structured tabular data

from typing import List, Dict
import csv


class CSVProcessor:
    """Class to handle CSV reading and processing."""

    @staticmethod
    def read_csv(file_path: str) -> List[Dict[str, str]]:
        """
        Read CSV file and return list of records.

        :param file_path: Path to CSV file
        :return: List of dictionaries
        """
        data: List[Dict[str, str]] = []

        try:
            with open(file_path, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print("File not found.")

        return data

    @staticmethod
    def calculate_average_salary(data: List[Dict[str, str]]) -> float:
        """Calculate average salary from CSV data."""
        if not data:
            return 0.0

        total = 0
        count = 0

        for row in data:
            try:
                total += float(row.get("salary", 0))
                count += 1
            except ValueError:
                continue

        return total / count if count else 0.0


def main() -> None:
    """Main execution function."""
    file_path = "employees.csv"

    data = CSVProcessor.read_csv(file_path)

    print("Data:", data)

    avg_salary = CSVProcessor.calculate_average_salary(data)

    print("Average Salary:", avg_salary)


if __name__ == "__main__":
    main()