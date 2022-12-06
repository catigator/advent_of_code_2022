import re
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
    rows = [[line[i] for i in range(1, len(line), 4)] for line in lines]
    return rows
    # rows = []
    # for line in lines:
    #     row = []
    #     for i in range(1, len(line), 4):
    #         row.append(line[i])
    #     rows.append(row)
    # return rows


def get_stacks(rows):
    stacks = defaultdict(list)
    for i_row in range(len(rows) -1, -1, -1):
        for i_stack, char in enumerate(rows[i_row]):
            if char != " ":
                stacks[i_stack].append(char)
    return stacks


def move_from_a_to_b(quantity: int, a: int, b: int):
    for i in range(quantity):
        to_move = a[-1]
        b += to_move
        a = a[:-1]

    return a, b


def move_from_a_to_b_many_at_once(quantity: int, a: int, b: int):

    to_move = a[-quantity:]
    b += to_move
    a = a[:-quantity]

    return a, b


def parse_command(command):
    new_command = re.findall('[0-9]+', command)
    new_command = [int(num) for num in new_command]
    return new_command


def handle_command(command, stacks, crate_mover=9000):
    a_i = command[1] - 1
    b_i = command[2] - 1
    quantity = command[0]

    if crate_mover == 9000:
        stacks[a_i], stacks[b_i] = move_from_a_to_b(quantity, stacks[a_i], stacks[b_i])
    elif crate_mover == 9001:
        stacks[a_i], stacks[b_i] = move_from_a_to_b_many_at_once(quantity, stacks[a_i], stacks[b_i])

    return stacks


def handle_commands(commands, stacks, crate_mover=9000):
    for command in commands:
        stacks = handle_command(command, stacks, crate_mover)


def get_commands_and_stacks(lines):

    split_lines = split_list_on_entry(lines, "")
    starting_stacks = [line for line in split_lines[0] if line[1] != "1"]
    commands = split_lines[1]
    rows = get_rows(starting_stacks)
    stacks = get_stacks(rows)
    commands = [parse_command(command) for command in commands]
    return commands, stacks


@time_it
def solve_part_1():
    print("Day 05 - Part 1")
    lines = read_input_lines_strip_newline(INPUT_FILENAME)
    commands, stacks = get_commands_and_stacks(lines)
    handle_commands(commands, stacks)
    top_crates = "".join([stack[-1] for key, stack in stacks.items()])
    print(stacks)
    print(f"The top crates are {top_crates}")


@time_it
def solve_part_2():
    print("Day 05 - Part 2")
    lines = read_input_lines_strip_newline(INPUT_FILENAME)
    commands, stacks = get_commands_and_stacks(lines)

    handle_commands(commands, stacks, crate_mover=9001)
    top_crates = "".join([stack[-1] for key, stack in stacks.items()])
    print(stacks)
    print(f"The top crates are {top_crates}")


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()