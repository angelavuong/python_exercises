'''
Name: Loops

Task:
Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1 <= i <= 10) should be printed on a new line in the form:
n x i = result.

Input:
A single integer n.

Output:
Print 10 lines of output; each line i contains the result of n x i.
'''

#!/bin/python3

import sys


n = int(input().strip())
for i in range(1,11):
    result = n * i
    print (str(n) + " x " + str(i) + " = " + str(result))
