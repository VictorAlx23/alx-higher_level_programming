#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        reversed_list = my_list
        reversed_list.reverse()

        for element in reversed_list:
            print("{:d}".format(element))
