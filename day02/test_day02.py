from day02 import get_puzzle_test_input, solution_part1, solution_part2


def test_part1():
    test_input = get_puzzle_test_input()
    assert solution_part1(test_input) == 1227775554


def test_part2():
    test_input = get_puzzle_test_input()
    assert solution_part2(test_input) == 4174379265
