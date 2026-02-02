# factorial-algorithms-and-probability
# Factorial Toolkit
A small Python package that implements multiple factorial algorithms, provides a command-line interface (CLI), includes automated tests, and benchmarks performance differences between implementations.

This project is intended as a clean, well-structured example of:

- Python packaging

- Algorithm comparison

- Testing with pytest

- integration with GitHub Actions

- Basic performance benchmarking

# Features
Three factorial implementations:
- Iterative
- Recursive
- Memoized

Command-line interface for computing factorials
Automated unit tests
Performance benchmarks
GitHub Actions CI pipeline
Editable install for local development

# Project strucutre
factorial_toolkit/
├── .github/
├── .pytest_cache/
├── .venv/
├── src/
│   └── factorial_toolkit/
│       ├── __init__.py
│       ├── factorial.py
│       └── cli.py
├── tests/
│   └── test_factorial.py
│   └── __init__.py
├── benchmarks/
│   └── benchmark_factorial.py
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── pyproject.toml
└── README.md
└── .gitignore
└──initial_code/

# Installation
Clone the repository and install the package in editable mode:
git clone https://github.com/beatrukzz/factorial-algorithms-and-probability.git
cd factorial-algorithms-and-probability/factorial_toolkit
python -m venv .venv
source .venv/bin/activate
pip install -e .

# Usage
# python API
from factorial_toolkit.factorial import (
    factorial,
    factorial_recursive,
    factorial_memo,
)

factorial(5)            # 120
factorial_recursive(5)  # 120
factorial_memo(5)       # 120

# Command-Line Interface
Run the CLI directly:
python -m factorial_toolkit.cli 5

Specify the algorithm:
python -m factorial_toolkit.cli 5 --method recursive
python -m factorial_toolkit.cli 5 --method memo

Available methods:
- iterative (default)
- recursiv
- memo

# testing
Run all tests with:
pytest

All tests are located in the tests/ directory and are automatically run in CI using GitHub Actions.

# Benchmarking
To compare performance of different implementations:
python benchmarks/benchmark_factorial.py

Example output:
Benchmarking factorial(10) with 1000 runs

iterative : 0.000785 seconds
recursive : 0.001579 seconds
memo      : 0.000155 seconds

Note:

Recursive and memoized implementations may hit Python’s recursion limit for large inputs.

Iterative implementation is the safest for large values of n.

# Continuous Integration
This project uses GitHub Actions to automatically:
- Install dependencies
- Run unit tests on every push and pull request to main

Workflow file:
.github/workflows/python-tests.yml

# Limitations
Recursive and memoized implementations are limited by Python’s recursion depth.

The project is intended for educational and demonstrative purposes rather than high-performance numerical computing.

# License
This project is released for educational use. No warranty is provided.
