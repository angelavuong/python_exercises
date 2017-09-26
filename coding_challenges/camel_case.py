'''
Name: CamelCase

Task:
Given s, print the number of words in s on a new line.

Input:
A single line containing string s.

Output:
Print the number of words in string s.
'''

#!/bin/python3

import sys
import string


s = input().strip()

print(sum(1 for c in s if c.isupper()) + 1)
    
