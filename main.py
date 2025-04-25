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
        raise RuntimeError(f"No puede ordenar {type(items)}")
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
        print("Uso: python main.py <filename> <remove_duplicates: yes/no> <order: asc/desc>")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(sort_list(word_list, dedupe=remove_duplicates))

