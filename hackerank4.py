#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    result = 0
    index = 0
    results_arr = []
    for i in range(0,len(arr)):
        current_number=arr[i]
        for each_elem in arr:
            result = each_elem+result
            
        result = result-current_number
        results_arr.append(result)
        result=0
    minimum = min(results_arr)
    maximum = max(results_arr)
    print(minimum,maximum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
