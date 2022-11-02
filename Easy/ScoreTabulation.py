import math
import os
import random
import re
import sys

#Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

#Example [12,24,10,24]

#Scores are in the same order as the games played. She tabulates her results as follows:

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    res = [0,0] #0 for max; #1 for min
    mini = scores[0]
    maxi = scores[0]
    for k in scores:
        if(mini > k):
            mini = k
            res[1] = res[1] + 1

        if(maxi < k):
            maxi = k
            res[0] = res[0] + 1

    return res
        
if __name__ == '__main__':

    result = breakingRecords([10,5,20,20,4,5,2,25,1])
    print(result)
