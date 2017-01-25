# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 23:35:41 2017

@author: wuhan
"""

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def full(li):
    d = len(li)
    i = 0
    while i < d:
        bo = False
        for e in li:
            if i + 1 == e:
                bo = True
                break
        if bo == False:
            break
        i = i + 1
    return bo

               
def check_sudoku(A):
    n = len(A)
    for p in A:
        for q in p:
            if not isinstance(q, int):
                return False
            if q < 1 or q > n:
                return False

    i = 0
    while i < n:
        if not full(A[i]):
            return False
        i = i + 1
    
    i = 0
    while i < n:
        m = []
        j = 0
        while j < n:
            m.append(A[j][i])
            j += 1
        if not full(m):
            return False
        i += 1
    return True


#print (check_sudoku(incorrect))
#>>> False

#print (check_sudoku(correct))
#>>> True

#print (check_sudoku(incorrect2))
#>>> False

#print (check_sudoku(incorrect3))
#>>> False

#print (check_sudoku(incorrect4))
#>>> False

#print (check_sudoku(incorrect5))
#>>> False

