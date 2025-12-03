from aoc2025.days.day02 import solve_part1, solve_part2
from aoc2025.utils.io import load_input


def test_part1_sample() -> None:
    input = load_input(day=2, sample=True)
    assert solve_part1(input) == 1227775554


def test_part2_sample() -> None:
    input = load_input(day=2, sample=True)
    assert solve_part2(input) == 4174379265


def test_part1() -> None:
    input = load_input(day=2, sample=False)
    assert solve_part1(input) == 19605500130


def test_part2() -> None:
    input = load_input(day=2, sample=False)
    assert solve_part2(input) == 36862281418
