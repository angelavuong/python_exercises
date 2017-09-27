'''

Name: Arrays

Task: Given an array, A, of N integers, print A in reverse order as a single line of space-separated numbers.

Input:
4
1 4 3 2

Output:
2 3 4 1
'''

#!/bin/python3

import sys

def FirstReverse(arr):
    return (arr[::-1])

n = int(input().strip())
arr = [arr_temp for arr_temp in input().strip().split(' ')]
result = FirstReverse(arr)
string = ' '.join(result)
print(string)
    
