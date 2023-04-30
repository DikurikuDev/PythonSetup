# Development Guidelines

The main goal of this project is to practice best practices for collaborating
with Python projects. The setup has TDD in mind, but you do not need to do it
in the PR. Just create a minimal test for the main feature, but maintaining
the coverage above 80% would be ideal. Also, try to keep the number of commits
low. Consider using squashing them and a more detailed git commit message.


## Requirements

- Python >= 3.9
- Poetry

## Getting started

```sh
## How to use poetry

# 1 - Install dependencies
$ poetry install
# 2 - Load dependencies
$ poetry shell
# to run tests
$ pytest ./
# to run tox
$ tox

# code formatter and linter will run at git commit
# however, you can run yourself

# to run code formatter
$ black ./
# to run code linter
$ flake8 ./

# to exit poetry shell (ctrl+d) or exit
```
