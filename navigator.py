"""
Navigator trough JSON file or object.
"""

import json
import doctest
import sys


def get_json(file_name: str):
    """
    Parsing file to get JSON data.
    >>> get_json("o.json")
    Sorry, something went wrong!
    """

    data = None

    try:
        with open(file_name, "r", encoding='utf-8') as file:
            data = json.load(file)
    except Exception:
        print("\nSorry, something went wrong!\nCheck the name of file.")
        sys.exit()

    return data


def get_type_name(name: str) -> str:
    """
    Normalize class name.
    # >>> get_type_name('<class 'str'>')
    """

    return name[8:-2]


def instruction():
    """
    Printing instructions.
    """

    print()
    print("Welcome to JSON Navigator!")
    print("The name of field to open content.")
    print("To go back type: `back`.")
    print("To exit type: `exit`")
    print()

    input("To start press ENTER")
    print()


def get_object(pos, path, data):
    """
    Get element from dict by the path.
    """

    if pos == len(path):
        return data

    return get_object(pos+1, path, data[path[pos]])


def action_request():
    """
    Get the action from user.
    """

    print()
    print("Please, print the field name to view / the object name to open / or back.")
    print(">>> ", end="")

    action = input()

    if action == 'exit':
        sys.exit()

    return action


def navigator(path: list, data):
    """
    Main navigator's function.
    """

    object_json = get_object(0, path, data)

    if isinstance(object_json, dict):
        for _, name in enumerate(list(object_json)):
            type_name = get_type_name(str(type(object_json[name])))
            print(name, "--", type_name)
    else:
        print(object_json)

    action = action_request()

    if action == 'back':
        path = path[:-1]
    else:
        if isinstance(object_json, dict):
            if action in list(object_json):
                path.append(action)

    navigator(path, data)


def main():
    """
    Just main function.
    """

    print("Enter file name with JSON content")
    print(">>> ", end="")
    filename = input()

    data = get_json(filename)

    instruction()
    navigator([], data)


if __name__ == '__main__':
    main()

doctest.testmod()
