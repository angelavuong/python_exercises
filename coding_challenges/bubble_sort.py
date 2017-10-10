'''

Name: Bubble Sort

Task: Given an array, a, of size N distinct elements, sort the array in ascending order using the Bubble Sort algorithm.

Print the following 3 lines:
1. Array is sorted in numSwap swaps.
2. First Element: firstElement
3. Last Element: lastElement

Sample Input:
3
1 2 3

Sample Output:
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
'''

#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
numberOfSwaps = 0
for j in range(n):
    for i in range(n-1):
        if(a[i] > a[i+1]):
            a[i], a[i+1] = a[i+1], a[i]
            numberOfSwaps += 1
        else:
            pass
print ('Array is sorted in ' + str(numberOfSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))
