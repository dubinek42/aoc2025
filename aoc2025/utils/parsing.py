def lines(text: str) -> list[str]:
    return text.splitlines()


def ints(text: str) -> list[int]:
    return [int(x) for x in text.split()]


def comma_separated_ints(line: str) -> list[int]:
    return [int(x) for x in line.split(",")]
