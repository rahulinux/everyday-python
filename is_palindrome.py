#!/usr/bin/env python


def is_palindrome(input_str):
   length = len(input_str)
   for i in range(length//2):
       if input_str[i] != input_str[~i]:
         return False
   return True

def is_palindrome_2(input_str):
    return input_str == input_str[::-1]




print is_palindrome("nitin")
print is_palindrome_2("nitin")
