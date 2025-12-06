from functools import reduce
from typing import Generator

from aoc2025.utils.parsing import lines

operators = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}


def solve_part1(input: str) -> int:
    z = zip(*[line.split() for line in lines(input)], strict=False)
    return sum(x for x in reduce_lines(z))


def solve_part2(input: str) -> int:
    return sum(reduce(operators[op], nums) for op, nums in parse_groups(lines(input)))


def reduce_lines(zipped: zip) -> Generator[int, None, None]:
    for item in zipped:
        yield reduce(operators[item[-1]], [int(i) for i in item[:-1]])


def parse_groups(ls: list[str]) -> Generator[tuple[str, list[int]], None, None]:
    max_len = max(len(x) for x in ls)
    current_group: list[list[str]] = []
    for i in range(max_len):
        line = list(x.ljust(max_len)[i] for x in ls)
        if is_empty_line(line):
            if current_group:
                yield parse_group(current_group)
            current_group = []
            continue
        current_group.append(line)
    if current_group:
        yield parse_group(current_group)


def parse_group(group: list[list[str]]) -> tuple[str, list[int]]:
    operator = group[0][-1]
    numbers = [int("".join(x[:-1])) for x in group]
    return operator, numbers


def is_empty_line(line: list[str]) -> bool:
    return all(x == " " for x in line)
