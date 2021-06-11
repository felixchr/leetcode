#!/usr/bin/env python3

def find_equal_index(mylist):
    len_of_list = len(mylist)
    if len_of_list <=  1:
        raise ValueError('Invalid list supplied')
    sum1 = mylist[0]
    sum2 = sum(mylist[1:])
    if sum1 == sum2:
        return 1
    for pointer in range(1, len_of_list-1):
        if sum1 == sum2:
            return pointer, sum1
        else:
            sum1, sum2 = sum1 + mylist[pointer], sum2 - mylist[pointer]
    return None
