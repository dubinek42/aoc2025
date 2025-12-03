from typing import Callable

from aoc2025.utils.parsing import lines, number_ranges


def solve_part1(input: str) -> int:
    input_lines = lines(input)
    ranges = number_ranges(input_lines[0])
    return sum(_count_invalid_in_range(r, _is_invalid) for r in ranges)


def solve_part2(input: str) -> int:
    input_lines = lines(input)
    ranges = number_ranges(input_lines[0])
    return sum(_count_invalid_in_range(r, _is_invalid2) for r in ranges)


def _is_invalid(id_str: str) -> int | None:
    if len(id_str) % 2 != 0:
        return None
    middle = len(id_str) // 2
    if id_str[:middle] == id_str[middle:]:
        return int(id_str)
    return None


def _is_invalid2(id_str: str) -> int | None:
    def has_repeating_pattern(s: str, pattern_len: int = 1) -> bool:
        if pattern_len > len(s) // 2:
            return False

        if len(s) % pattern_len == 0:
            pattern = s[:pattern_len]
            if pattern * (len(s) // pattern_len) == s:
                return True

        return has_repeating_pattern(s, pattern_len + 1)

    if has_repeating_pattern(id_str):
        return int(id_str)
    return None


def _count_invalid_in_range(
    range_item: list[str], func: Callable[[str], int | None]
) -> int:
    return sum(result for x in range_item if (result := func(x)) is not None)
