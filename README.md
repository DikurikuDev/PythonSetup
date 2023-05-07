# Python Setup

A personal boilerplate setup for Python projects.

## Requirements

- Python >= 3.9
- Poetry

## Features and tools

- Hide ignored files and folders on VSCode
- VSCode and Poetry configurations for importation and auto-completion work
seamlessly
- Multiple Python versions configuration, code formatting, code linting, code
testing, and test coverage on GitHub Action (main branch only)
- Tox configuration to work alongside Poetry
- Code formatting (Black) and Code linting (Flake8)
- Dependency management (Poetry)
- Automated testing configuration (Tox)

## Getting started



```sh
#  to run the code:
#  1 - Install dependencies.
$ poetry install
#  2 - Load dependencies.
$ poetry shell
#  Now you can use Python and the dependencies installed.
$ python ./src/main.py
#  To run tests:
$ pytest ./
#  To exit poetry shell (ctrl+d) or:
$ exit

# -----

#  Before starting a new project:
#  Make sure that when you commit, the code formatter and linter will run
# automatically. If not:
$ pre-commit install

# -----

#  Before push to main, is nice to text if tox is working
$ tox

# -----

#  The code formatter and linter will run at git commit. However, you can run
# yourself:

#  To run code formatter:
$ black ./
#  To run code linter
$ flake8 ./
```
