import numpy as np

from aoc2025.utils.parsing import bits_array


def solve_part1(input: str) -> int:
    rolls_of_paper = bits_array(input)
    return sum(
        1
        for x in range(rolls_of_paper.shape[0])
        for y in range(rolls_of_paper.shape[1])
        if rolls_of_paper[x][y] == 1 and neighbors_count(rolls_of_paper, x, y) < 4
    )


def solve_part2(input: str) -> int:
    rolls_of_paper = bits_array(input)
    number_of_rolls = int(rolls_of_paper.sum())
    while True:
        new_rolls = remove_accessible(rolls_of_paper)
        if (new_rolls == rolls_of_paper).all():
            break
        rolls_of_paper = new_rolls

    removed_total = number_of_rolls - int(rolls_of_paper.sum())
    return removed_total


def neighbors_count(arr: np.ndarray, x: int, y: int) -> int:
    rows, cols = arr.shape
    neighbor_coords = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    ]
    return sum(
        int(arr[r][c]) for r, c in neighbor_coords if 0 <= r < rows and 0 <= c < cols
    )


def remove_accessible(arr: np.ndarray) -> np.ndarray:
    result = arr.copy()
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            if arr[x][y] == 1 and neighbors_count(arr, x, y) < 4:
                result[x][y] = 0
    return result
