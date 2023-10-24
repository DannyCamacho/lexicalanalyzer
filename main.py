#! /usr/bin/env python3

import re


def read_items(filename):
    item_list = []
    with open(filename) as file:
        for line in file:
            item_list.append(line)
    return item_list


def parse(code):
    tokens = []  # list to store tuples of (lexeme, token)
    for line in code:  # for loop to grab each line of code individually
        line = re.split("//", line)[0]  # removes comments by taking first part of split
        line = re.sub("^\s+|\s+$", "", line)  # removes leading/trailing whitespace
        line = re.split('\s+', line)  # splits line up by whitespace
        for item in line:  # for loop to grab each item within the line of code
            lexemes = re.findall("[+]", item)
            for lexeme in lexemes:
                tokens.append(lexeme)
    return tokens


def main():
    code = read_items("code.txt")
    tokens = parse(code)
    for token in tokens:
        print(f"\"{token}\" = {token}")


if __name__ == "__main__":
    main()
