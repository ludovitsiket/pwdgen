#!/usr/bin/python3
import random
import sys
import argparse


def abeceda():
    m_pismena = ["a", "b", "c", "d", "e", "f", "g",
                 "h", "i", "j", "k", "l", "m", "n", "o",
                 "p", "q", "r", "s", "t", "u", "v", "w", "x",
                 "y", "z"]

    symboly = [".", "!", "?", "_", "-", ";", "/", "=", "*",
               "@", "#", "$", "%", "^", "&", " ", "+"]

    cisla = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    v_pismena = ["A", "B", "C", "D", "E", "F", "G",
                 "H", "I", "J", "K", "L", "M", "N", "O",
                 "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                 "Y", "Z"]
    return m_pismena, symboly, v_pismena, cisla


def multi_replace(content, to_replace, repl):
    for elem in to_replace:
        if elem in content:
            content = content.replace(elem, repl)
    return content


def counting_lenght(abc):
    index = 1
    indexed_list = []
    while index <= len(abc):
        value = str(len("list" + str(index)))
        indexed_list.append(value)
        index += 1
    whole_min = int(min(indexed_list[0], indexed_list[1], indexed_list[2], indexed_list[3]))
    return indexed_list[0], indexed_list[1], indexed_list[2], indexed_list[3], whole_min


def make_pwd(l1, l2, l3, l4, some_list):
    rnd1 = random.randrange(int(l1))
    rnd2 = random.randrange(int(l2))
    rnd3 = random.randrange(int(l3))
    rnd4 = random.randrange(int(l4))
    some_list += (male_pismena[rnd1], znaky[rnd2], velke_pismena[rnd3], cislice[rnd4])
    return some_list


def pwdgen_help():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-l', '--length', action="store", dest="l", type=int, help="number of password length, max 79")
    parser.print_help()


if __name__ == '__main__':
    try:
        dlzka_hesla = abs(int(sys.argv[1]))
        male_pismena, znaky, velke_pismena, cislice = abeceda()
        m, z, v, c, pwd_len = counting_lenght(abeceda())
        whole_list = []
        counter = 0
        while counter < pwd_len:
            whole_list = make_pwd(m, z, v, c, whole_list)
            counter += 1
        heslo = str(whole_list[0:dlzka_hesla])
        heslo = multi_replace(heslo, [',', "'", ' ', '[', ']'], '')
        print(heslo)
    except (IndexError, ValueError):
        pwdgen_help()
