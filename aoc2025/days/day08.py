import itertools
import math

from aoc2025.utils.parsing import comma_separated_ints_tuples, lines

NUMBER_OF_PAIRS_TO_JOIN = 1000


class Circuit:
    def __init__(self, boxes: set[tuple[int, ...]]) -> None:
        self.boxes = boxes

    def can_join(self, other: "Circuit") -> bool:
        return bool(self.boxes & other.boxes)

    def join(self, other: "Circuit") -> "Circuit":
        return Circuit(self.boxes.union(other.boxes))

    def __repr__(self) -> str:
        return f"{self.boxes}"


def solve_part1(input: str) -> int:
    boxes = [comma_separated_ints_tuples(line) for line in lines(input)]
    circuits = []
    for x in all_distances_sorted(boxes)[:NUMBER_OF_PAIRS_TO_JOIN]:
        circuits.append(Circuit({x[1], x[2]}))
        circuits = join_all(circuits)
    counts = sorted([len(c.boxes) for c in circuits], reverse=True)[:3]
    return math.prod(counts)


def solve_part2(input: str) -> int:
    boxes = [comma_separated_ints_tuples(line) for line in lines(input)]
    circuits = []
    for x in all_distances_sorted(boxes):
        circuits.append(Circuit({x[1], x[2]}))
        circuits = join_all(circuits)
        if len(circuits) == 1 and all(b in circuits[0].boxes for b in boxes):
            return math.prod((x[1][0], x[2][0]))
    return -1


def euclidean_distance(box1: tuple[int, ...], box2: tuple[int, ...]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(box1, box2, strict=False)))


def all_distances_sorted(
    boxes: list[tuple[int, ...]],
) -> list[tuple[float, tuple[int, ...], tuple[int, ...]]]:
    all_distances = [
        (euclidean_distance(a, b), a, b) for a, b in itertools.combinations(boxes, 2)
    ]
    return sorted(all_distances)


def join_all(circuits: list[Circuit]) -> list[Circuit]:
    changed = True
    while changed:
        changed = False
        for i, c in enumerate(circuits):
            for j, d in enumerate(circuits[i + 1 :], start=i + 1):
                if c.can_join(d):
                    circuits[i] = c.join(d)
                    circuits.pop(j)
                    changed = True
                    break
            if changed:
                break
    return circuits
