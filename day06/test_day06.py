from pathlib import Path

import pytest

from day06 import (
    RESULT_PART1,
    RESULT_PART2,
    TEST_RESULT_PART1,
    TEST_RESULT_PART2,
    get_puzzle_input,
    get_puzzle_test_input,
    solution_part1,
    solution_part2,
)

PART2_TOO_LOW_VALUE1 = 10227753241159


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
def test_part2_with_known_false_solutions():
    puzzle_input = get_puzzle_input(Path(__file__))
    assert solution_part2(puzzle_input) > PART2_TOO_LOW_VALUE1


@pytest.mark.skip(reason="Known solution test - skip unless needed")
def test_part2_with_known_solution():
    puzzle_input = get_puzzle_input(Path(__file__))
    assert solution_part2(puzzle_input) == RESULT_PART2
