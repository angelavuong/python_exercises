'''

Name: Recursion Factorial

Input:
A single integer N (argument to pass into factorial)

Sample Input:
3

Sample Output:
6

3 * 2 * 1 = 6
'''

#!/bin/python3

import sys

def factorial(n):
    # Complete this function
    if (n <= 1):
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
