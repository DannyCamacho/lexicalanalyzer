#! /usr/bin/env python3

import re


def read_items(filename):
    item_list = []
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            item_list.append(line)
    return item_list


def parse(code):
    tokens = []
    for line in code:
        line = line.split("//")[0]
        print(line)
    return tokens


def main():
    code = read_items("code.txt")
    tokens = parse(code)
    for token in tokens:
        print(f"\"{token[0]}\" = {token[1]}")


if __name__ == "__main__":
    main()
