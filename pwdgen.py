#!/usr/bin/python3
import argparse
import sys
import random


def dict_keys(values):
    key_length = len(values)
    x = 0
    k = []
    while x < key_length:
        k.append(x)
        x += 1
    return k


def dict_values():
    values = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", ".", "!", "?", "_", "-", ";", "/", "=", "*", "@", "#", "$", "%", "^", "&", " ",
              "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G",
              "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return values


def make_dict(list1, list2):
    result = dict(zip(list1, list2))
    return result


def multi_replace(content, to_replace, repl):
    for elem in to_replace:
        if elem in content:
            content = content.replace(elem, repl)
    return content


def pwdgen_help():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-l', '--length', action="store", dest="l", type=int, help="number of password length, max 79")
    parser.print_help()


def make_password(value_length, values, length):
    iterator = 0
    password = []
    while iterator < value_length:
        dict_key = (random.randrange(length))
        password.append(values.get(dict_key))
        iterator += 1
    return str(password)


if __name__ == '__main__':
    try:
        password_length = abs(int(sys.argv[1]))
        val = dict_values()
        keys = dict_keys(dict_values())
        result_dict = make_dict(keys, val)
        pwd = make_password(password_length, result_dict, len(result_dict))
        nice_pwd = multi_replace(pwd, '[,],' ',' "'" ' ', '')
        print(nice_pwd)
    except (IndexError, ValueError):
        pwdgen_help()
