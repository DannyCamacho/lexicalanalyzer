#! /usr/bin/env python3

import re  # import regular expressions


def read_items(filename):  # read_items() function
    item_list = []  # list to store each line of txt file
    with open(filename) as file:  # open file for reading
        for line in file:  # for loop to access each line of txt file
            item_list.append(line)  # append line to item_list
    return item_list  # return item_list


def build_dict(token_list):
    token_dict = {}  # dictionary to store lexeme-token pairs
    for token in token_list:  # for loop to add each lexeme-token combination
        token = token.split(' ')  # split at comma
        token_dict[token[0]] = token[1].strip()  # add to dictionary and strip whitespace
    return token_dict  # return token_dict


def parse(code_list):  # parse() function
    lexeme_list = []  # list to store tuples of (lexeme, token)
    for line in code_list:  # for loop to grab each line of code individually
        line = re.split("//", line)[0]  # removes comments by taking first part of split
        line = re.sub("^\s+|\s+$", "", line)  # removes leading/trailing whitespace
        line = re.split('\s+', line)  # splits line up by inner whitespace
        for item in line:  # for loop to grab each item within the line of code
            lexemes = re.split("(\W)", item)  # split at non-word characters
            lexemes = list(filter(None, lexemes))  # remove empty items from list
            for lexeme in lexemes:  # for loop to access each lexeme
                lexeme_list.append(lexeme)  # append lexeme to lexemes
    return lexeme_list  # return lexeme_list


def main():  # main() function
    token_dict = build_dict(read_items("lexeme_list.txt"))  # build dict from lexeme_list.txt
    lexeme_list = parse(read_items("code.txt"))  # get lexeme list from code.txt
    for lexeme in lexeme_list:  # for loop to access each lexeme in the lexeme list
        if lexeme in token_dict:  # if the lexeme exists in the dictionary
            print(f"\"{lexeme}\" = {token_dict[lexeme]}")  # print the lexeme-token combination
        elif re.match(r'^([\s\d]+)$', lexeme):  # else if current lexeme is made up of only digits
            print(f"\"{lexeme}\" = {'integer'}")  # print the lexeme as integer
        elif re.match(r'([^\W]+)$', lexeme):  # else if current lexeme is made up of word characters
            print(f"\"{lexeme}\" = {'identifier'}")  # print the lexeme as identifier
        else:  # else used to catch unaccounted for cases
            print(f"\"{lexeme}\" = {'*ERROR*'}")  # print the lexeme as an error


if __name__ == "__main__":  # if we are in current file
    main()  # run main from current file
