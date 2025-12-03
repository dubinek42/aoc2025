from aoc2025.utils.parsing import letter_and_number, lines


class Dial:
    START = 50
    MAX = 99

    def __init__(self) -> None:
        self.value = self.START
        self.zeros_end = 0
        self.zeros_passed = 0

    def turn(self, direction: str, steps: int) -> None:
        for _ in range(steps):
            self.step(direction)
        if self.value == 0:
            self.zeros_end += 1

    def step(self, direction: str) -> None:
        if direction == "L":
            self.value -= 1
        elif direction == "R":
            self.value += 1
        self.value = self.value % (self.MAX + 1)
        if self.value == 0:
            self.zeros_passed += 1


def solve_part1(input: str) -> int:
    dial = Dial()
    input_lines = lines(input)
    for line in input_lines:
        direction, steps = letter_and_number(line)
        dial.turn(direction, steps)
    return dial.zeros_end


def solve_part2(input: str) -> int:
    dial = Dial()
    input_lines = lines(input)
    for line in input_lines:
        direction, steps = letter_and_number(line)
        dial.turn(direction, steps)
    return dial.zeros_passed
