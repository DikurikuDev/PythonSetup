# STEAMWORLD EXTRACTOR

A extractor/compressor tool to handle SteamWorld compressed files.

## Games supported

- SteamWorld Dig 2
- SteamWorld Heist
- SteamWorld Quest Hand of Gilgamech

## Getting Started

### Requirements

- Poetry

### How to use poetry

```sh
# to install dependencies
$ poetry install

# to use python with dependencies
$ poetry shell
$ python

# to exit poetry shell
$ exit
```

### Testing

```sh
# inside poetry shell
$ pytest ./test/**/*
```

### Formatting

```sh
# inside poetry shell
$ black ./test/
```
### Linting

```sh
# inside poetry shell
$ flake8 ./test/
```
