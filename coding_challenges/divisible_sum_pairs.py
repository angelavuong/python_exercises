'''
Name: Divisible Sum Pairs

Task:
You are given an array of n integers and a positive integer k.
Find and print the number of (i,j) pairs where i < j and ai + aj is divisible by k.

Input:
The first line contains 2 space-separated integers, n and k, respectively.
The second line contains n space-separated integers describing the respective values of a0, a1, an

Output:
Print the number of (i,j) pairs where i < j and ai + aj is evenly divisible by k.
'''

#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    counter = 0
    for i in range(n):
        pointer = ar[i]
        i+=1
        for j in range(i,n):
            if((pointer + ar[j])%k == 0):
                counter +=1
            else:
                pass
    return counter


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
