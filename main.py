#! /usr/bin/env python3

import re  # import regular expressions


def read_file(filename):  # read_file() function: read from file and store into list
    item_list = []  # list to store each line of txt file
    with open(filename) as file:  # open file for reading
        for line in file:  # for loop to access each line of txt file
            item_list.append(line)  # append line to item_list
    return item_list  # return item_list


def build_dict(token_list):  # build_dict() function: build dictionary from given list
    token_dict = {}  # dictionary to store lexeme-token pairs
    for token in token_list:  # for loop to add each lexeme-token combination
        token = re.split('\s+', token)  # split at whitespace
        token_dict[token[0]] = token[1]  # add to dictionary and strip whitespace
    return token_dict  # return token_dict


def parse(code_list):  # parse() function: traverse list to separate into individual lexemes
    lexeme_list = []  # list to store tuples of (lexeme, token)
    for line_of_code in code_list:  # for loop to grab each line_of_code of code individually
        line_of_code = re.split("//", line_of_code)  # splits line_of_code up at // (comment)
        line_of_code = re.split('\s+', line_of_code[0])  # splits first part of line_of_code up by whitespace
        for item in line_of_code:  # for loop to grab each item within the line_of_code of code
            lexemes = re.split("(\W)", item)  # split at non-word characters
            for lexeme in list(filter(None, lexemes)):  # for loop to access each non-empty element of lexemes
                lexeme_list.append(lexeme)  # append lexeme to lexemes
    return lexeme_list  # return lexeme_list


def main():  # main() function
    token_dict = build_dict(read_file("lexeme_token_pairs.txt"))  # build dict from lexeme_token_pairs.txt
    lexeme_list = parse(read_file("code.txt"))  # get lexeme list from code.txt
    for lexeme in lexeme_list:  # for loop to access each lexeme in the lexeme list
        if lexeme in token_dict:  # if the lexeme exists in the dictionary
            print(f"\"{lexeme}\" = {token_dict[lexeme]}")  # print the lexeme-token combination
        elif re.match(r'^([\d]+)$', lexeme):  # else if current lexeme is made up of only digits
            print(f"\"{lexeme}\" = {'integer'}")  # print the lexeme as integer
        elif re.match(r'([^\W]+)$', lexeme):  # else if current lexeme is made up of word characters
            print(f"\"{lexeme}\" = {'identifier'}")  # print the lexeme as identifier
        else:  # else used to catch unaccounted for cases
            print(f"\"{lexeme}\" = {'*ERROR*'}")  # print the lexeme as an error


if __name__ == "__main__":  # if we are in current file
    main()  # run main from current file
