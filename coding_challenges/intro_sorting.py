'''
Name: Intro to Sorting

Input:
V = the value that has to be searched
n = the size of the array
ar = numbers that make up the array

Output:
The index of V in the array


Sample Input:
4
6
1 4 5 7 9 12

Sample Output:
1
'''

V = int(input().strip())
n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
for i in range(n):
    if (arr[i] == V):
        print (i)
    else: pass
