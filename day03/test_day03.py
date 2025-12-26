from day03 import (
    TEST_RESULT_PART1,
    TEST_RESULT_PART2,
    get_puzzle_test_input,
    solution_part1,
    solution_part2,
)


def test_part1():
    test_input = get_puzzle_test_input()
    assert solution_part1(test_input) == TEST_RESULT_PART1


def test_part2():
    test_input = get_puzzle_test_input()
    assert solution_part2(test_input) == TEST_RESULT_PART2
