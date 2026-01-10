import logging
import sys
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day04.log"
# TODO-ARA: Set test results, when known
TEST_RESULT_PART1 = 13
TEST_RESULT_PART2 = -1


def get_puzzle_test_input():
    return [
        [0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    ]


def get_puzzle_input(script_path: Path) -> list[list[int]]:
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
    return [[0 if char == "." else 1 for char in line.strip()] for line in lines]


def count_neighbouring_rolls(row, column, rows, columns, puzzle_input):
    # count neighboring 1s = rolls
    neighbours = 0
    for n_row in range(row - 1, row + 2):
        for n_column in range(column - 1, column + 2):
            if n_row < rows and n_row >= 0 and n_column < columns and n_column >= 0:
                neighbours += puzzle_input[n_row][n_column]
    # remove 1, since algorithm counts the center roll in every case
    return neighbours - 1


def solution_part1(puzzle_input: list[list[int]]) -> int:
    logging.debug("solution_part1")
    rows = len(puzzle_input)
    columns = len(puzzle_input[0])
    max_neighbour_count = 4
    count_movable_rolls = 0
    for row in range(0, rows):
        for column in range(0, columns):
            if puzzle_input[row][column] == 1:
                count_neighbours = count_neighbouring_rolls(
                    row, column, rows, columns, puzzle_input
                )
                if count_neighbours < max_neighbour_count:
                    count_movable_rolls += 1

    return count_movable_rolls


def solution_part2(puzzle_input: list[list[int]]) -> int:
    logging.debug("solution_part2")
    pass


if __name__ == "__main__":
    args = setup_parser(LOGFILENAME)
    day_solution = DaySolution(
        get_puzzle_test_input=get_puzzle_test_input,
        get_puzzle_input=partial(get_puzzle_input, Path(__file__)),
        solution_part1=solution_part1,
        solution_part2=solution_part2,
    )
    run_solutions(args, day_solution)
