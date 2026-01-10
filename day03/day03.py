import logging
import sys
from functools import partial
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).parent.parent))

from aoc_utils import DaySolution, run_solutions, setup_parser

LOGFILENAME = "day03.log"
TEST_RESULT_PART1 = 357
TEST_RESULT_PART2 = 3121910778619


def get_puzzle_test_input():
    return [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]


def test_part1():
    test_input = get_puzzle_test_input()
    assert solution_part1(test_input) == TEST_RESULT_PART1


def test_part2():
    test_input = get_puzzle_test_input()
    assert solution_part2(test_input) == TEST_RESULT_PART2


def get_puzzle_input(script_path: Path) -> list[str]:
    input_path = script_path.parent / "input.txt"
    with open(input_path) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def find_max_pair(line: str) -> int:
    max_value = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            value = int(line[i] + line[j])
            if value > max_value:
                max_value = value
    logging.debug(f"Max pair in line '{line}' is\n{max_value}")
    return max_value


def find_max_twelve_digit_number(line: str) -> int:
    DIGIT_COUNT = 12
    if len(line) < DIGIT_COUNT:
        raise ValueError(
            f"Cannot find max {DIGIT_COUNT} digit number in line with less than 12 characters."
        )
    max_chars = ""
    left_index = 0
    right_index = -DIGIT_COUNT + 1  # start by cutting off 11 chars from the line

    for i in range(0, DIGIT_COUNT):
        used_line = line[left_index:right_index]

        logging.debug(f"line: {line}")
        logging.debug(f"used_line: {used_line}")
        logging.debug(f"left_index: {left_index} - right_index: {right_index}")

        (new_left_index, new_max_char) = find_leftmost_max_digit_in_string(used_line)
        max_chars += new_max_char
        left_index += new_left_index + 1

        if right_index is not None:
            right_index += 1
        # right_index needs to be set to None when the end of the string is reached
        if right_index == 0:
            right_index = None

    return int(max_chars)


def find_leftmost_max_digit_in_string(line: str) -> tuple[int, str]:
    max_char = ""
    max_value = 0
    max_index = -1
    for c_index, c in enumerate(line):
        c_value = int(c)
        if c_value > max_value:
            max_char = c
            max_value = c_value
            max_index = c_index
    logging.debug(
        f"in line '{line}' leftmost max char is '{max_char}' at index {max_index}"
    )
    return (max_index, max_char)


def solution_part1(puzzle_input: list[str]) -> int:
    logging.debug("solution_part1")
    max_pairs = []
    for line in puzzle_input:
        max_pairs.append(find_max_pair(line))
    return sum(max_pairs)


def solution_part2(puzzle_input: list[str]) -> int:
    logging.debug("solution_part2")
    max_numbers = []
    for line in puzzle_input:
        max_numbers.append(find_max_twelve_digit_number(line))
    logging.debug(f"array max_numbers: {max_numbers}")
    return sum(max_numbers)


if __name__ == "__main__":
    args = setup_parser(LOGFILENAME)
    day_solution = DaySolution(
        get_puzzle_test_input=get_puzzle_test_input,
        get_puzzle_input=partial(get_puzzle_input, Path(__file__)),
        solution_part1=solution_part1,
        solution_part2=solution_part2,
    )
    run_solutions(args, day_solution)
