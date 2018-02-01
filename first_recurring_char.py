#!/usr/bin/env python

# Return first reccuring char from string


input_str = raw_input("Enter String :- ")


def first_recurring_char(input_str):

    data = {}
    for char in input_str:
        if char in data:
           return char
        data[char] = 1


print first_recurring_char(input_str)

