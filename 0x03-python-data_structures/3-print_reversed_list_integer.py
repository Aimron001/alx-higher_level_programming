#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints all integers in a list in reverse'''
    my_list.reverse()
    for i in my_list:
        print("{}".format(i))
