#!/usr/bin/env python

"""
Check for balanced parentheses in an expression
Given an expression string exp , write a program to examine 
whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are 
correct in exp. For example, the program should print true 
for exp = “[()]{}{[()()]()}” and false for exp = “[(])”
"""



import sys

def isBalanced(s):
    # Complete this function
    opening_str = "{[("
    closing_str = "}])"
    start = ""
    for char in s:
        if char in opening_str:
            start += char
        elif char in closing_str:
            char_index = opening_str.index(start[-1])
            if char_index != closing_str.index(char):
                return "NO"
            else:
                start = start[:-1]
    return "YES"

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        result = isBalanced(s)
        print result
