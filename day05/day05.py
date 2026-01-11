import logging
import sys
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day05.log"
TEST_RESULT_PART1 = 3
TEST_RESULT_PART2 = 14
# Expected results for the actual puzzle input - received after solving the puzzle
RESULT_PART1 = 744
RESULT_PART2 = 347468726696961


def parse_input_lines(lines: str) -> tuple[list[str], list[str]]:
    breakline = False
    ranges = []
    orders = []
    for line in lines:
        line = line.strip()
        if line == "":
            breakline = True
            continue
        if breakline:
            orders.append(line)
        else:
            ranges.append(line)
    return ranges, orders


def get_puzzle_test_input() -> tuple[list[str], list[str]]:
    lines = [
        "3-5\n",
        "10-14\n",
        "16-20\n",
        "12-18\n",
        "\n",
        "1\n",
        "5\n",
        "8\n",
        "11\n",
        "17\n",
        "32\n",
    ]
    return parse_input_lines(lines)


def get_puzzle_input(script_path: Path) -> tuple[list[str], list[str]]:
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
    return parse_input_lines(lines)


def convert_ranges_to_tuples(ranges: list[str]) -> list[tuple[int, int]]:
    range_tuples = []
    for r in ranges:
        lower, higher = r.split("-")
        range_tuples.append((int(lower), int(higher)))
    return range_tuples


def solution_part1(puzzle_input: tuple[list[str], list[str]]) -> int:
    logging.debug("solution_part1")
    ranges_raw = puzzle_input[0]
    orders = [int(order) for order in puzzle_input[1]]
    ranges = convert_ranges_to_tuples(ranges_raw)
    # ingredients are fresh, if their order number can be found in the given ranges
    fresh_ingredients = 0
    for order in orders:
        for rs in ranges:
            if rs[0] <= order <= rs[1]:
                fresh_ingredients += 1
                break

    return fresh_ingredients


def sort_and_consolidate_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_ranges = ranges.copy()
    sorted_ranges.sort(key=lambda r: r[0])
    consolidated_ranges = []

    rp_current = sorted_ranges[0]
    for i in range(1, len(sorted_ranges)):
        low_current, high_current = rp_current
        rp_next = sorted_ranges[i]
        low_next, high_next = rp_next

        # no range overlap
        if high_current < low_next:
            consolidated_ranges.append(rp_current)
            rp_current = rp_next
        else:
            # range overlap
            high_current = max(high_current, high_next)
            rp_current = (low_current, high_current)

    # append the last rp_current
    consolidated_ranges.append(rp_current)
    return consolidated_ranges


def count_fresh_ingredients(ranges: list[tuple[int, int]]) -> int:
    count = 0
    for rs in ranges:
        count += 1 + rs[1] - rs[0]
    return count


def solution_part2(puzzle_input: tuple[list[str], list[str]]) -> int:
    logging.debug("solution_part2")
    ranges_raw = puzzle_input[0]
    ranges = convert_ranges_to_tuples(ranges_raw)
    consolidated_ranges = sort_and_consolidate_ranges(ranges)
    fresh_id_amount = count_fresh_ingredients(consolidated_ranges)
    return fresh_id_amount


if __name__ == "__main__":
    args = setup_parser(LOGFILENAME)
    day_solution = DaySolution(
        get_puzzle_test_input=get_puzzle_test_input,
        get_puzzle_input=partial(get_puzzle_input, Path(__file__)),
        solution_part1=solution_part1,
        solution_part2=solution_part2,
    )
    run_solutions(args, day_solution)
