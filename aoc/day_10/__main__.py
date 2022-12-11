from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_10/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_10/EXAMPLE_01.txt"

def process_lines(split_lines):
    cycle = 0
    adds = []
    x = 1
    for line in split_lines:
        cycle += 1
        command = line[0]
        if command != "noop":
            if command == "addx":
                num = int(line[1])
                adds.append((cycle+2, num))
        to_delete = []
        for i, add in enumerate(adds):
            if add[0] == cycle:
                x += add[1]
                to_delete.append(i)
        for i in to_delete:
            adds = adds.pop(i)
    print(f"X is {x} after {cycle} cycles")

    for just_looping_through_the_last_cycles in range(3):
        cycle += 1
        for i, add in enumerate(adds):
            if add[0] == cycle:
                x += add[1]
                to_delete.append(i)

    return x, cycle

@time_it
def solve_part_1():
    print("Day 10 - Part 1")
    lines = read_input_lines(EXAMPLE_FILENAME)
    split_lines = [line.split() for line in lines]
    x, cycle = process_lines(split_lines)
    print(x, cycle)


@time_it
def solve_part_2():
    print("Day 10 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()