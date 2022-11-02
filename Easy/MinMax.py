#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    mini = arr[0]
    maxi = arr[0]
    sumMin = 0
    sumMax = 0
    i=0
    for k in arr:
        if(k<mini):
            mini=k
        if(k>maxi):
            maxi=k
    for k in arr:
        i=i+1
        if(mini==maxi):
            if(i<=4):
                sumMin = sumMin + k
                sumMax = sumMax + k
        else:
            if(k!=maxi):
                sumMin = sumMin + k
            if(k!=mini):
                sumMax = sumMax + k
    print(sumMin,sumMax, sep=" ")
    
            
if __name__ == '__main__':

    arr = [1,3,5,7,9]

    miniMaxSum(arr)
