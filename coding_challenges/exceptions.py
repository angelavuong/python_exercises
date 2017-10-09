'''

Name: Exceptions

Tasks: Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

Sample Input:
3

Sample Output:
3

Sample Input:
za

Sample Output:
Bad string
'''

#!/bin/python3

import sys


S = input().strip()
try:
    value = int(S)
    print (S)
except:
    print ('Bad String')
