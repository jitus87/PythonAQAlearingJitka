# A module is a file with some Python code. We use modules to break up our progam into multiple files. Code is better organized. Each file is a module.
# This file will use the code from file: converters.py but only some functions, not all

from converters import kg_to_lbs    # Ctrl + space

print(kg_to_lbs(100))  # because we imported only specific function, we don' t need to write converters.kg_to_lbs

