'''

Name: Binary Numbers

Task: Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in n's binary representation.

Sample Input:
5
Sample Output:
1

Sample Input:
13
Sample Output:
2
'''

#!/bin/python3

import sys
def binary_conversion(n):
    binary = []
    while(n>0):
        remainder = int(n%2)
        binary.append(remainder)
        n = int((n-remainder)/2)

    max_value = 0
    count = 0
    for i in range(len(binary)):
        if (binary[i] == 1):
            count +=1
            if(max_value <= count):
                max_value = count
        else:
            count = 0

    return max_value

n = int(input().strip())
total = binary_conversion(n)
print (total)
