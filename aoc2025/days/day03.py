from aoc2025.utils.parsing import lines, str_to_digits


def solve_part1(input: str) -> int:
    input_lines = lines(input)
    return sum(highest_jolt(x) for x in input_lines)


def solve_part2(input: str) -> int:
    input_lines = lines(input)
    return sum(highest_jolt(x, 12) for x in input_lines)


def highest_jolt(bank: str, turns: int = 2) -> int:
    bank_values = list(enumerate(str_to_digits(bank)))
    sorted_bank_by_value = sorted(bank_values, key=lambda x: x[1], reverse=True)

    def find_highest(
        bank: list[tuple[int, int]], current_joltage: int, remaining_turns: int
    ) -> int:
        if remaining_turns == 0:
            return current_joltage
        if len(bank) < remaining_turns:
            return -1
        for battery in bank:
            right_part = list(filter(lambda x: x[0] > battery[0], bank))
            new_joltage = current_joltage + (battery[1] * 10 ** (remaining_turns - 1))
            if (
                result := find_highest(right_part, new_joltage, remaining_turns - 1)
            ) != -1:
                return result
        return -1

    return find_highest(sorted_bank_by_value, 0, turns)
