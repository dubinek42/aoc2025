def lines(text: str) -> list[str]:
    return text.splitlines()


def ints(text: str) -> list[int]:
    return [int(x) for x in text.split()]


def comma_separated_ints(line: str) -> list[int]:
    return [int(x) for x in line.split(",")]


def letter_and_number(line: str) -> tuple[str, int]:
    return line[0], int(line[1:])
