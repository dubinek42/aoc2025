from aoc2025.days.day01 import solve_part1, solve_part2
from aoc2025.utils.io import load_input


def test_part1_sample():
    input = load_input(day=1, sample=True)
    assert solve_part1(input) == 3


def test_part2_sample():
    input = load_input(day=1, sample=True)
    assert solve_part2(input) == 6


def test_part1():
    input = load_input(day=1, sample=False)
    assert solve_part1(input) == 1147


def test_part2():
    input = load_input(day=1, sample=False)
    assert solve_part2(input) == 6789
