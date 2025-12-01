from aoc2025.utils.io import load_input
from aoc2025.utils.parsing import lines


def solve_part1(input: str) -> int:
    input_lines = lines(input)
    return len(input_lines)


def run(sample: bool = False) -> None:
    input = load_input(day=1, sample=sample)
    print(solve_part1(input))


if __name__ == "__main__":
    run()
