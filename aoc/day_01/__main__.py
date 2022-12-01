from typing import List

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix,
    read_input_int_split_on_empty_line
)


INPUT_FILENAME = "aoc/day_01/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_01/EXAMPLE_01.txt"


def get_largest_sum(parts: List):
    return max([sum(part) for part in parts])

@time_it
def solve_part_1():
    print("Day 01 - Part 1")
    split_lines = read_input_int_split_on_empty_line(INPUT_FILENAME)
    max_part = get_largest_sum(split_lines)
    print(f"The elf carrying the most calories is carrying {max_part} calories")


@time_it
def solve_part_2():
    print("Day 01 - Part 2")
    split_lines = read_input_int_split_on_empty_line(INPUT_FILENAME)
    sums = [sum(part) for part in split_lines]
    ordered_sums = sorted(sums, reverse=True)
    max_three = sum(ordered_sums[:3])
    print(f"The three elves carrying the most calories are carrying {max_three} calories")


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()