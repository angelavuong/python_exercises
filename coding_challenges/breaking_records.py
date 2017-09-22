'''
Name: Breaking Records
Task:
Maria plays n games of college basketball in a season. Because she wants to go pro, she tracks her points scored per game sequentially in an array defined as
score = [s0,s1...sn]. After each game i, she checks to see if score si breaks her record for most or least points scored so far during that season.

Output:
Find and print the number of times she breaks her record for most and least points scored during the season.
'''

#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    max_value = s[0]
    min_value = s[0]
    max_counter = 0
    min_counter = 0
    record = []
    for i in range(len(s)):
        if (s[i]>max_value):
            max_counter += 1
            max_value = s[i]
        elif(s[i]<min_value):
            min_counter += 1
            min_value = s[i]
        else:
            pass
    record.append(max_counter)
    record.append(min_counter)
    return record

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
