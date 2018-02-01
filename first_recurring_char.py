#!/usr/bin/env python

# Return first reccuring char from string


input_str = raw_input("Enter String :- ")


def first_recurring_char(input_str):

    counts = {}
    for char in input_str:
        if char in counts:
           return char
        counts[char] = 1


print first_recurring_char(input_str)

