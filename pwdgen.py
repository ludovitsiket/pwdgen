#!/usr/bin/python3
import argparse
import sys
import random


def abeceda():
    alphabet = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g",
                8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o",
                16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x",
                25: "y", 26: "z",
                27: ".", 28: "!", 29: "?", 30: "_", 31: "-", 32: ";", 33: "/", 34: "=", 35: "*",
                36: "@", 37: "#", 38: "$", 39: "%", 40: "^", 41: "&", 42: " ", 43: "+",
                44: "0", 45: "1", 46: "2", 47: "3", 48: "4", 49: "5", 50: "6", 51: "7", 52: "8", 53: "9",
                54: "A", 55: "B", 56: "C", 57: "D", 58: "E", 59: "F", 60: "G",
                61: "H", 62: "I", 63: "J", 64: "K", 65: "L", 66: "M", 67: "N", 68: "O",
                69: "P", 70: "Q", 71: "R", 72: "S", 73: "T", 74: "U", 75: "V", 76: "W", 77: "X",
                78: "Y", 79: "Z"}
    return alphabet


def multi_replace(content, to_replace, repl):
    for elem in to_replace:
        if elem in content:
            content = content.replace(elem, repl)
    return content


def pwdgen_help():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-l', '--length', action="store", dest="l", type=int, help="number of password length, max 79")
    parser.print_help()


def collect_values():
    full_dict = abeceda()
    whole_length = len(full_dict)
    return full_dict, whole_length


def make_password(value_length, values, length):
    iterator = 0
    password = []
    while iterator < value_length:
        dict_key = (random.randrange(length))
        password.append(values.get(dict_key))
        iterator += 1
    return password


if __name__ == '__main__':
    try:
        password_length = abs(int(sys.argv[1]))
        dictionary, dictionary_length = collect_values()
        pwd = make_password(password_length, dictionary, dictionary_length)
        print(pwd)
    except (IndexError, ValueError):
        pwdgen_help()
