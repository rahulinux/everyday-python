#!/usr/bin/env python



def bubble_sort(data):
   for i in range(len(data)-1):
     for j in range(len(data) - 1 - i):
        if data[j] > data[j+1]:
           data[j+1],data[j] = data[j],data[j+1]
   return data



print bubble_sort([1,3,2,5,4,10,7])
