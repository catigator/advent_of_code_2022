ADVENT OF CODE 2022

# Installation

1. Install conda
2. Create conda environment with `conda create --name aoc_2022 python=3.11 --channel conda-forge`
3. Install conda environment with `conda env update`
4. Activate conda environment with `conda activate aoc_2022`
5. Install `browser-cookie3` with `pip install browser-cookie3`

# Testing

Run with e.g. `python -m pytest` or `pytest aoc/day_01`

# Download Stuff

First log in to Advent of code (https://adventofcode.com/ ) in your browser so that the cookies from there can be used.

Download the input, puzzle description and examples for a specific day with:

```commandline
python -m utils.downloader <day: int>
```

e.g.

```commandline
python -m utils.downloader 4
```

and they will be downloaded to `aoc/day_{day}/` as `INPUT.md`, `PUZZLE.md` and `EXAMPLE_X.md`.

NOTE: On Mac (macOS 12.6) I had to follow the instructions at https://stackoverflow.com/questions/33699577/conda-update-fails-with-ssl-error-certificate-verify-failed/57305648#57305648 and set the 
REQUESTS_CA_BUNDLE environment variable to the certificate used when visiting adventofcode.com. This messes with e.g. `pip`
installations so it's easiest to just run once locally in a terminal before using the downloader, as opposed to adding it to `.zshrc`

# Instructions

Run with e.g. `python -m aoc.day_04` from root folder after activating the conda environment.

If you want to save the output to a file, the easiest way is to run `python -m aoc.day_04 | tee aoc/day_04/output.log`