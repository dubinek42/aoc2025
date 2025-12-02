from aoc2025.days.day02 import solve_part1, solve_part2
from aoc2025.utils.io import load_input


def test_part1_sample():
    input = load_input(day=2, sample=True)
    assert solve_part1(input) == 1227775554
