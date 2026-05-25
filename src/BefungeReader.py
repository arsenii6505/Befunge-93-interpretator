import os

class BefungeReader:
    @staticmethod
    def load(filepath: str) -> list[list[str]]:
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding="UTF-8") as f:
                current_map = []
                for row in f.readlines():
                    row_map = []
                    for char in row:
                        row_map.append(char)
                    current_map.append(row_map)
            return current_map
        raise FileNotFoundError(filepath)