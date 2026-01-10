from pathlib import Path

import pytest

from day03 import (
    TEST_RESULT_PART1,
    TEST_RESULT_PART2,
    get_puzzle_input,
    get_puzzle_test_input,
    solution_part1,
    solution_part2,
)

# Expected results for the actual puzzle input - received after solving the puzzle
RESULT_PART1 = 17166
RESULT_PART2 = 169077317650774


def test_part1():
    test_input = get_puzzle_test_input()
    assert solution_part1(test_input) == TEST_RESULT_PART1


def test_part2():
    test_input = get_puzzle_test_input()
    assert solution_part2(test_input) == TEST_RESULT_PART2


@pytest.mark.skip(reason="Known solution test - skip unless needed")
def test_part1_with_known_solution():
    puzzle_input = get_puzzle_input(Path(__file__))
    assert solution_part1(puzzle_input) == RESULT_PART1


@pytest.mark.skip(reason="Known solution test - skip unless needed")
def test_part2_with_known_solution():
    puzzle_input = get_puzzle_input(Path(__file__))
    assert solution_part2(puzzle_input) == RESULT_PART2
