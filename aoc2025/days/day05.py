from aoc2025.utils.parsing import (
    ints,
    number_ranges_from_lines,
    two_parts_separated_by_empty_line,
)


def solve_part1(input: str) -> int:
    lines1, lines2 = two_parts_separated_by_empty_line(input)
    ranges = number_ranges_from_lines(lines1)
    ingredients = ints(lines2)

    result = 0
    for i in ingredients:
        if is_fresh(i, ranges):
            result += 1
    return result


def solve_part2(input: str) -> int:
    lines1, _ = two_parts_separated_by_empty_line(input)

    ranges = number_ranges_from_lines(lines1)
    i = 0
    while i < len(ranges):
        should_stop = False
        for r in ranges:
            joined = join_range(ranges[i], r)
            if joined != ranges[i]:
                ranges[i] = joined
                ranges.remove(r)
                should_stop = True
                break
        if should_stop:
            i = 0
            continue
        i += 1
    ranges_set = set(ranges)
    result = 0
    for r in ranges_set:
        if r[0] == r[1]:
            result += 1
            continue
        result += r[1] - r[0] + 1
    return result


def is_fresh(ingredient: int, ranges: list[tuple[int, int]]) -> bool:
    return any(low <= ingredient <= high for low, high in ranges)


def join_range(range1: tuple[int, int], range2: tuple[int, int]) -> tuple[int, int]:
    low1, high1 = range1
    low2, high2 = range2
    if low1 <= low2 <= high1:
        return low1, max(high1, high2)
    if low2 <= low1 <= high2:
        return low2, max(high1, high2)
    return range1
