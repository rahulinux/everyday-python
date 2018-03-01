#!/usr/bin/env python


"""
You are given an m x n 2D image matrix (List of Lists) 
where each integer represents a pixel. 
Flip it in-place along its vertical axis.
"""

def flip_it(matrix):
   for r in range(len(matrix)):
     temp = []
     c = len(matrix[r]) - 1
     while c >= 0:
        temp.append(matrix[r][c])
        c -= 1
     matrix[r] = temp
   return matrix
        

def flip_it2(matrix):
   for i in range(len(matrix)):
      matrix[i] = matrix[i][::-1]
   return matrix
      



m = [[1, 0, 0], [0, 0, 1]]
print m
print flip_it(m)
print m
#print flip_it2(m)
