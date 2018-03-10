#!/usr/bin/env python


def bubble_sort(input_list):
    swap = True
    while swap:
        swap = False
        for i in range(len(input_list)-1):
          if input_list[i] > input_list[i+1]:
              input_list[i],input_list[i+1] = input_list[i+1],input_list[i]
              swap = True
    return input_list


print bubble_sort([4,2,1,8,3,10,0])
