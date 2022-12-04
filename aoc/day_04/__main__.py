from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_04/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_04/EXAMPLE_01.txt"


def overlaps(elf_1, elf_2):
    if elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]:
        return True
    elif elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[1]:
        return True
    return False


def overlaps_at_all(a, b):
    if a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]:
        return True
    elif b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]:
        return True
    return False


@time_it
def solve_part_1():
    print("Day 04 - Part 1")
    lines = read_input_lines(INPUT_FILENAME, True)
    split_lines = [line.split(",") for line in lines]
    overlapping = 0
    for line in split_lines:
        split_line = [line[0].split("-"), line[1].split("-")]
        elf_1 = (int(split_line[0][0]), int(split_line[0][1]))
        elf_2 = (int(split_line[1][0]), int(split_line[1][1]))
        overlapping += overlaps(elf_1, elf_2)

    print(f"There are {overlapping} overlapping pairs")


@time_it
def solve_part_2():
    print("Day 04 - Part 2")
    lines = read_input_lines(INPUT_FILENAME, True)
    split_lines = [line.split(",") for line in lines]
    overlapping = 0
    for line in split_lines:
        split_line = [line[0].split("-"), line[1].split("-")]
        elf_1 = (int(split_line[0][0]), int(split_line[0][1]))
        elf_2 = (int(split_line[1][0]), int(split_line[1][1]))
        overlapping += overlaps_at_all(elf_1, elf_2)

    print(f"There are {overlapping} overlapping pairs")


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()