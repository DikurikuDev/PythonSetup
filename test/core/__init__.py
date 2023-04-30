from os import getcwd
from os.path import join
from sys import path

module_path = join(getcwd(), "src/core")
path.append(module_path)
