from collections import defaultdict

from aoc2025.utils.parsing import array_2d


def solve_part1(input: str) -> int:
    array = array_2d(input)
    ys = {_find_start(array)}
    splits = 0

    for x in range(1, len(array)):
        ys_next = set()
        for y in ys:
            if array[x][y] == ".":
                ys_next.add(y)
            if array[x][y] == "^":
                splits += 1
                ys_next.add(y - 1)
                ys_next.add(y + 1)
        ys = ys_next

    return splits


def solve_part2(input: str) -> int:
    array = array_2d(input)
    start_y = _find_start(array)
    ys = {start_y}
    possible_ways = defaultdict(int)
    possible_ways[start_y] = 1

    for x in range(1, len(array)):
        ys_next = set()
        for y in ys:
            if array[x][y] == ".":
                ys_next.add(y)
            if array[x][y] == "^":
                ys_next.add(y - 1)
                ys_next.add(y + 1)
                possible_ways[y - 1] += possible_ways[y]
                possible_ways[y + 1] += possible_ways[y]
                possible_ways[y] = 0

        ys = ys_next

    return sum(v for v in possible_ways.values() if v > 0)


def _find_start(array: list[list[str]]) -> int:
    return array[0].index("S")
