import sys

from src.Operations import MAP, Operations
from src.BefungeReader import BefungeReader

class BefungeMachine:
    def __init__(self, filepath):
        self.mapSize = [25, 80]
        self.pointerPos = [0, 0]
        self.direction = "R"
        self.stack = []
        self.map = [[" " for _ in range(self.mapSize[1])] for __ in range(self.mapSize[0])]
        self.string_mode = False
        self.activated = False
        self.load_map(BefungeReader.load(filepath))

    def run(self):
        self.activated = True
        while self.activated:
            y, x = self.pointerPos
            char = self.map[y][x]
            self.invoke(char)

    def clear_map(self):
        self.map = [[" " for _ in range(self.mapSize[1])] for __ in range(self.mapSize[0])]

    def load_map(self, new_map: list[list[str]]):
        self.clear_map()
        for i in range(len(new_map)):
            for j in range(len(new_map[i])):
                self.map[i][j] = new_map[i][j]

    def invoke(self, char: str):
        if char == '"':
            Operations.toggle_string(self)
        elif self.string_mode:
            self.stack.append(ord(char))
            Operations.empty_operation(self)
        elif char.isdigit():
            self.stack.append(int(char))
            Operations.empty_operation(self)
        elif char in MAP:
            MAP[char](self)
        else:
            Operations.empty_operation(self)

    def change_direction(self, direction):
        if direction == "R" or direction == "L" or direction == "U" or direction == "D":
            self.direction = direction
        else:
            raise ValueError(f"Wrong direction {direction}, allowed only R,L,U,D")

    def push_stack(self, item):
        self.stack.append(item)

    def pop_stack(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return 0

    def get_map(self, y: int, x: int) -> int:
        if self.is_in_map(y, x):
            return ord(self.map[y][x])
        return 0

    def set_map(self, y: int, x: int, item: int):
        if self.is_in_map(y, x):
            self.map[y][x] = chr(item % 256)

    def is_in_map(self, y: int, x: int) -> bool:
        return 0 <= y < self.mapSize[0] and 0 <= x < self.mapSize[1]

    @staticmethod
    def get_int_input() -> int:
        line = sys.stdin.readline()
        return int(line) if line.isdigit() else 0

    @staticmethod
    def get_input() -> str:
        return sys.stdin.read(1)

    @staticmethod
    def print_int_output(num: int):
        sys.stdout.write(str(num) + " ")
        sys.stdout.flush()

    @staticmethod
    def print_output(char: str):
        sys.stdout.write(char)
        sys.stdout.flush()