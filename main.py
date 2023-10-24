#! /usr/bin/env python3

import re  # import regular expressions


def read_items(filename):  # read_items() function
    item_list = []  # list to store each line of txt file
    with open(filename) as file:  # open file for reading
        for line in file:  # for loop to access each line of txt file
            item_list.append(line)  # append line to item_list
    return item_list  # return item_list


def parse(code):  # parse() function
    lexeme_list = []  # list to store tuples of (lexeme, token)
    for line in code:  # for loop to grab each line of code individually
        line = re.split("//", line)[0]  # removes comments by taking first part of split
        line = re.sub("^\s+|\s+$", "", line)  # removes leading/trailing whitespace
        line = re.split('\s+', line)  # splits line up by whitespace
        for item in line:  # for loop to grab each item within the line of code
            lexemes = re.split("[\W]", item)  # split at non-word characters
            lexemes += re.findall("[\W]", item)  # find all non-word characters
            lexemes = list(filter(None, lexemes))  # remove empty items from list
            for lexeme in lexemes:  # for loop to access each lexeme
                lexeme_list.append(lexeme)  # append lexeme to lexemes
    return lexeme_list  # return lexeme_list


def main():  # main() function
    code = read_items("code.txt")
    token_list = read_items("lexeme_list.txt")
    token_dict = {}
    for token in token_list:
        token = token.split(',')
        token_dict[token[0]] = token[1].strip()
    lexemes = parse(code)
    for lexeme in lexemes:
        if lexeme in token_dict:
            print(f"\"{lexeme}\" = {token_dict[lexeme]}")
        elif re.match(r'^([\s\d]+)$', lexeme):  # else if current lexeme is made up of only digits
            print(f"\"{lexeme}\" = {'integer'}")
        elif re.match(r'([^\W]+)$', lexeme):  # else if current lexeme is made up of word characters
            print(f"\"{lexeme}\" = {'identifier'}")
        else:
            print(f"\"{lexeme}\" = {'*ERROR*'}")


if __name__ == "__main__":  # if we are in current file
    main()  # run main from current file
