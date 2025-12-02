from typing import Generator


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
