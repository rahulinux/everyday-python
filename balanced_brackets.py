#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        if len(start) <= 0 and char in closing_str:
            return "NO"
        elif char in opening_str:
            start += char
        elif char in closing_str:
            char_index = opening_str.index(start[-1])
            if char_index != closing_str.index(char):
                return "NO"
            else:
                start = start[:-1]
    if len(start) != 0:
      return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(raw_input().strip())
    results = []
    for a0 in xrange(t):
        s = raw_input().strip()
        result = isBalanced(s)
        results.append(result)
        print result
    with open("/tmp/out","w") as f:
       f.write('\n'.join(results))
