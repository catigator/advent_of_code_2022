from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_10/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_10/EXAMPLE_02.txt"


def process_lines(split_lines):
    cycle = 0
    signal_strengths = []
    x = 1

    for line in split_lines:
        command = line[0]

        if command != "noop":

            if cycle + 1 == 20 or (cycle + 1 - 20) % 40 == 0:
                signal_strength = (cycle+1) * x
                signal_strengths.append(signal_strength)

            cycle += 2

            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)

            val = int(line[1])
            x += val
        else:
            cycle += 1

            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)

        if cycle > 220:
            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_strength = cycle * x
                signal_strengths.append(signal_strength)
            break

    print(f"X is {x} after {cycle} cycles")
    signal_sum = sum(signal_strengths)
    print(f"The sum of these signal strengths is {signal_sum}")

    return x, cycle, signal_strengths


@time_it
def solve_part_1():
    print("Day 10 - Part 1")
    lines = read_input_lines(INPUT_FILENAME)
    split_lines = [line.split() for line in lines]
    x, cycle, signal_strengths = process_lines(split_lines)
    print(f"The signal strength total is {sum(signal_strengths)}")
    print(x, cycle)


@time_it
def solve_part_2():
    print("Day 10 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()