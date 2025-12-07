from typing import Generator

import numpy as np


def lines(text: str) -> list[str]:
    return text.splitlines()


def ints(text: str) -> list[int]:
    return [int(x) for x in text.split()]


def comma_separated_ints(line: str) -> list[int]:
    return [int(x) for x in line.split(",")]


def comma_separated_strs(line: str) -> list[str]:
    return line.split(",")


def letter_and_number(line: str) -> tuple[str, int]:
    return line[0], int(line[1:])


def number_ranges(line: str) -> Generator[list[str], None, None]:
    for range_item in comma_separated_strs(line):
        low, high = range_item.split("-")
        yield list(str(x) for x in range(int(low), int(high) + 1))


def number_ranges_from_lines(lines: str) -> list[tuple[int, int]]:
    result = []
    for line in lines.splitlines():
        low, high = line.split("-")
        result.append((int(low), int(high)))
    return result


def number_ranges_ints_from_lines(lines: str) -> Generator[int, None, None]:
    for range_item in lines.splitlines():
        low, high = range_item.split("-")
        for i in range(int(low), int(high) + 1):
            yield i


def str_to_digits(line: str) -> list[int]:
    return [int(x) for x in line]


def bits_array(text: str) -> np.ndarray:
    """Parse lines of `.` and `@` into a 2D numpy array."""

    rows = [line.strip() for line in text.splitlines() if line.strip()]
    data = [[1 if ch == "@" else 0 for ch in row] for row in rows]
    return np.array(data, dtype=int)


def array_2d(text: str) -> list[list[str]]:
    rows = [line.strip() for line in text.splitlines() if line.strip()]
    data = [[ch for ch in row] for row in rows]
    return data


def two_parts_separated_by_empty_line(text: str) -> tuple[str, str]:
    parts = text.split("\n\n")
    return parts[0], parts[1]
