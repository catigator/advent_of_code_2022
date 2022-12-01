import pytest
from aoc.day_01.__main__ import INPUT_FILENAME, EXAMPLE_FILENAME, get_largest_sum
from utils.helper_functions import read_input_int_split_on_empty_line


class TestPart1:

    def test_part_1(self):
        split_lines = read_input_int_split_on_empty_line(EXAMPLE_FILENAME)
        max_part = get_largest_sum(split_lines)
        assert max_part == 24000

@pytest.mark.skip(reason="Not implemented yet")
class TestPart2:

    def test_part_2(self):
        assert False