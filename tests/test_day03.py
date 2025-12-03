import pytest

from aoc2025.days.day03 import highest_jolt


@pytest.mark.parametrize(
    "bank,expected,turns",
    [
        ("987654321111111", 98, 2),
        ("811111111111119", 89, 2),
        ("234234234234278", 78, 2),
        ("818181911112111", 92, 2),
        ("987654321111111", 987654321111, 12),
        ("811111111111119", 811111111119, 12),
        ("234234234234278", 434234234278, 12),
        ("818181911112111", 888911112111, 12),
    ],
)
def test_highest_jolt(bank: str, turns: int, expected: int) -> None:
    assert highest_jolt(bank, turns) == expected
