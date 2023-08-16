#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    a = set(my_list)
    for b in a:
        add += b
    return add
