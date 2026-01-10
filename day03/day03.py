import logging
import sys
from functools import partial
from pathlib import Path

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
    """
    Find the maximum twelve-digit number that can be formed from the digits in
    the line.
    This alghorithm uses a sliding window approach to find the leftmost maximum
    digit for each position in the twelve-digit number.
    This makes sure that the resulting number is the largest possible by always
    choosing the highest available digit at each step.
    """
    digit_count = 12
    if len(line) < digit_count:
        raise ValueError(
            f"Cannot find max {digit_count} digit number in line with less than {digit_count} characters."
        )
    max_chars = ""
    left_index = 0
    right_index = -digit_count + 1  # start by cutting off 11 chars from the line

    for i in range(0, digit_count):
        used_line = line[left_index:right_index]

        logging.debug(f"line: {line}")
        logging.debug(f"used_line: {used_line}")
        logging.debug(
            f"Cannot find max {digit_count}-digit number in line with fewer than {digit_count} characters."
        )

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
