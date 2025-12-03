import argparse
import importlib
import time

from aoc2025.utils.io import load_input


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="Day (1-12)")
    parser.add_argument("--part", type=int, choices=[1, 2], help="Part (1 or 2)")
    parser.add_argument("--sample", action="store_true", help="Use sample input")
    args = parser.parse_args()

    module_name = f"aoc2025.days.day{args.day:02d}"
    module = importlib.import_module(module_name)

    input_text = load_input(day=args.day, sample=args.sample)

    start_time = time.perf_counter()
    if args.part in (None, 1):
        result1 = module.solve_part1(input_text)
        print(
            f"Day {args.day:02d}, Part 1: {result1}, Time: {(time.perf_counter() - start_time):.4f} s"
        )
        start_time = time.perf_counter()
    if args.part in (None, 2):
        result2 = module.solve_part2(input_text)
        print(
            f"Day {args.day:02d}, Part 2: {result2}, Time: {(time.perf_counter() - start_time):.4f} s"
        )
