#!/usr/bin/env python


# Generate Random complex password depends on user input


import argparse
import random
from string import punctuation

# GLOBAL Vars

alphabet = [ chr(i) for i in range(ord('a'),ord('z')+1)  ]
special_char =  [ i for i in punctuation ]  
numbers = range(9)

def parse_input():
    """parse command line argument"""
    parser = argparse.ArgumentParser(description='Generate random complex password')
    parser.add_argument('--length', help='password length (default: 8)',default=8,type=int)
    parser.add_argument('--level', help='complexity level (default: 5) \
                           means it will add special char, int, CAPS alpha',default=3, type=int)
    args = parser.parse_args()
    return args


def generate_passwd(length,level):
    mypwd = []
    for i in range(length):
        rand_level = random.randrange(level+1)
        if rand_level <= 1: 
           mypwd = mypwd + [ alphabet[random.randrange(len(alphabet))] ]
        elif rand_level == 2:
           mypwd = mypwd + [random.randrange(len(alphabet))]
        elif rand_level == 3:
           string =  alphabet[random.randrange(len(alphabet))] 
           mypwd = mypwd + [ string.capitalize()  ]
        elif rand_level == 4:
           mypwd = mypwd + [special_char[random.randrange(len(special_char))] ]
    return mypwd



if __name__ == '__main__': 
    input_data = parse_input()
    length = input_data.length
    level = input_data.level
    print ''.join( str(i) for i in generate_passwd(length,level))
