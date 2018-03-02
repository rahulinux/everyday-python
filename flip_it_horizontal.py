#!/usr/bin/env python



def flip_it(matrix):
    # return matrix[::-1]
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    temp = 0
    i = 0
    while i <= r/2:
        j = 0
        while j <= c:
            temp = matrix[i][j]
            matrix[i][j] = matrix[r-i][j]
            matrix[r-i][j] = temp
            j = j+1
        i = i + 1
    return matrix


def flip_it_2(matrix):
   if len(matrix) <= 1:
     return matrix
   x = len(matrix) - 1
   i = 0
   while x > 0:
     matrix[x],matrix[i] = matrix[i],matrix[x]
     x -= 1 
     i += 1
   return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]

print "Before", matrix
print flip_it_2(matrix)
