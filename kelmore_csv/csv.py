import csv
import os
from typing import List, Dict, Optional

CSVRows = List[List[str]]
CSVDict = List[Dict[str, Optional[str]]]


class CSVTools:

    @staticmethod
    def to_json(full_path: str) -> CSVDict:
        all_rows: List[List[str]] = CSVTools.to_rows(full_path)
        headers: List[str] = all_rows.pop(0)

        return CSVTools._create_json_map_helper(headers, all_rows)

    @staticmethod
    def to_rows(full_path: str) -> CSVRows:
        output: List[List[str]] = []

        with open(full_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                output.append(row)

        return output

    @staticmethod
    def _create_json_map_helper(headers: List[str], rows: List[List[str]]) -> CSVDict:
        output: CSVDict = []
        for row in rows:
            new_row: Dict[str, Optional[str]] = {}
            for idx, header in enumerate(headers):
                if idx < len(row):
                    value: str = row[idx]
                    if not value:
                        value = None
                else:
                    value = None

                new_row[header] = value

            output.append(new_row)

        return output


class CSVWrapper:
    file_path: str
    file_name: str

    def __init__(self, full_path: str):
        self.file_path = full_path
        self.file_name = os.path.basename(full_path)

    def json(self) -> CSVDict:
        return CSVTools.to_json(self.file_path)

    def rows(self) -> CSVRows:
        return CSVTools.to_rows(self.file_path)
