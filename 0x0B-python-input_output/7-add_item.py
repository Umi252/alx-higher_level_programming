#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.

Uses save_to_json_file and load_from_json_file functions.
The list is saved as a JSON representation in a file named add_item.json.
If the file doesn’t exist, it will be created.
No file permissions/exceptions are managed.
"""

import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_arguments_to_list():
    """Add arguments to a list and save them to a JSON file."""
    args = sys.argv[1:]
    if exists('add_item.json'):
        my_list = load_from_json_file('add_item.json')
    else:
        my_list = []

    my_list.extend(args)

    save_to_json_file(my_list, 'add_item.json')
    print(f'Arguments added to the list: {args}')


if __name__ == "__main__":
    add_arguments_to_list()
