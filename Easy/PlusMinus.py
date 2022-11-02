#!/bin/python3

#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
#Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    countZero = countMinus = countPlus = 0
    for k in arr:
        if(k==0):
            countZero = countZero + 1
        elif(k<0):
            countMinus = countMinus + 1
        else:
            countPlus = countPlus + 1
            
    print(f'{countPlus/len(arr):.6f}')         
    print(f'{countMinus/len(arr):.6f}')
    print(f'{countZero/len(arr):.6f}')
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = [1,1,0,-1,-1]

    plusMinus(arr)
