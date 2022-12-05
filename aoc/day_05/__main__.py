from collections import defaultdict
from typing import List

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix, read_input_lines_strip_newline, split_list_on_entry
)


INPUT_FILENAME = "aoc/day_05/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_05/EXAMPLE_01.txt"


def get_rows(lines):
    rows = []
    for line in lines:
        row = []
        for i in range(1, len(line), 4):
            row.append(line[i])
        rows.append(row)
    return rows


def get_stacks(rows):
    stacks = defaultdict(list)
    for i_row in range(len(rows)):
        for i_stack, char in enumerate(rows[i_row]):
            stacks[i_stack].append(char)
    return stacks

@time_it
def solve_part_1():
    lines = read_input_lines_strip_newline(EXAMPLE_FILENAME)
    split_lines = split_list_on_entry(lines, "")
    starting_stacks = [line for line in split_lines[0] if line[1] != "1"]
    commands = split_lines[1]
    rows = get_rows(starting_stacks)
    stacks = get_stacks(rows)
    print(lines)
    print(stacks)
    print("Day 05 - Part 1")


@time_it
def solve_part_2():
    print("Day 05 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()