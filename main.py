"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True


def sort_list(items, ascending=True, dedupe=DEFAULT_DUPLICATES):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    if dedupe:
        items = list(set(items))
        
    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending_order = DEFAULT_ASCENDING

    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        ascending_order = sys.argv[3].lower() == "asc"
    else:
        print("The file must be specified as the first argument")
        print("The second argument indicates if you want to remove duplicates")
        sys.exit(1)

    print(f"Words will be read from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(sort_list(word_list, dedupe=remove_duplicates))

