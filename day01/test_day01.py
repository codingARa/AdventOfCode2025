from day01 import get_puzzle_test_input, solution_part1, solution_part2


def test_part1():
    test_input = get_puzzle_test_input()
    assert solution_part1(test_input) == 3


def test_part2():
    test_input = get_puzzle_test_input()
    assert solution_part2(test_input) == 6
    assert solution_part2(test_input) == 6
