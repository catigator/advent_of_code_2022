from typing import List

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_03/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_03/EXAMPLE_01.txt"


# def split_sentences(lines):
#     temp = []
#     for line in lines:
#         hl = int(len(line)/2)
#         temp.append([line[:hl], line[:hl]])
#     return temp

def get_value(c: str):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


def get_duplicate(a: str, b: str):

    dups = ""
    for char_a in a:
        if char_a in b and char_a not in dups:
            dups += char_a

    for char_b in b:
        if char_b in char_a not in dups:
            dups += char_b

    return dups


def solve_lines_1(lines: List[str]):
    split_lines = [[line[:int(len(line)/2)], line[int(len(line)/2):]] for line in lines]
    total = 0
    for line in split_lines:
        dup = get_duplicate(line[0], line[1])
        value = get_value(dup)
        total += value
    return total

@time_it
def solve_part_1():
    print("Day 03 - Part 1")
    lines = read_input_lines(INPUT_FILENAME, True)
    total = solve_lines_1(lines)
    print(f"The sum of priorities for duplicate items is {total}")


@time_it
def solve_part_2():
    print("Day 03 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()