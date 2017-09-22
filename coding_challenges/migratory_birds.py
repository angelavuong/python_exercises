'''
Name: Migratory Birds

Task:
A flock of n birds is flying across the continent. Each bird has a type, and the different types are designated by ID: 1,2,3,4,5.

Input:
The first line contains an integer denoting n (number of birds).
The second line contains n space-separated integers describing the respective type number of each bird in the flock.

Output:
Given an array of n integers where each integer describes the type of bird in the flock, find and print the type of number of the
most common bird. If two or more types of birds are equally common, choose the type with the smallest ID number.
'''

#!/bin/python3

import sys
from collections import Counter

def migratoryBirds(n, ar):
    # Complete this function
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    for i in range(n):
        if(ar[i] == 1):
            count_1 += 1
        elif(ar[i] == 2):
            count_2 += 1
        elif(ar[i] == 3):
            count_3 += 1
        elif(ar[i] == 4):
            count_4 += 1
        elif(ar[i] == 5):
            count_5 += 1
    find_max = max(count_1,count_2,count_3,count_4,count_5)
    if(find_max == count_1): return 1
    elif(find_max == count_2): return 2
    elif(find_max == count_3): return 3
    elif(find_max == count_4): return 4
    elif(find_max == count_5): return 5

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
