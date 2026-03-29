# UC7 – Handle nested JSON objects and perform data extraction and transformation

from typing import List, Dict, Any


class JSONTransformer:
    """Class to handle nested JSON transformation."""

    @staticmethod
    def transform(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Transform nested JSON into flat structure.

        :param data: Nested JSON data
        :return: Flattened data
        """
        result: List[Dict[str, Any]] = []

        for item in data:
            try:
                employee = item.get("employee", {})
                name = employee.get("name", "Unknown")
                salary = employee.get("salary", 0)

                result.append({
                    "name": name,
                    "salary": salary
                })
            except Exception:
                continue

        return result


def main() -> None:
    """Main execution function."""
    data: List[Dict[str, Any]] = [
        {"employee": {"name": "Alice", "salary": 50000}},
        {"employee": {"name": "Bob", "salary": 60000}},
        {"employee": {"name": "Charlie"}},  # missing salary
    ]

    print("Original Data:", data)

    transformed = JSONTransformer.transform(data)

    print("Transformed Data:", transformed)


if __name__ == "__main__":
    main()