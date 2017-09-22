'''
Name: Kangaroo
Task:
Given kangaroo 1's location (x1) and velocity (v1) and kangaroo 2's location (x2) and velocity (v2), return 'YES' if they ever land in the same
spot on the same jump or 'NO' if they don't.

Output:
- 'YES' or 'NO'
'''

#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if(x1 > x2 and v1 > v2):
        return 'NO'
    else:
        if(v1 > v2 and ((x2-x1)%(v1-v2) == 0)):
            return 'YES'
        else:
            return 'NO'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
