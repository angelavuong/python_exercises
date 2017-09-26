'''
Name: Fibonacci Modified

Input:
A single line of three space-separated integers describing the respective values of t1, t2, n.

Output:
tn = t1 + t2**2 up to n = 5


Sample Input:
0 1 5

Sample Output:
5
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

lst = list(map(int, input().strip().split(' ')))
t1 = lst[0]
t2 = lst[1]
n = lst[2]
odd = True
for i in range(n-2):
    result = t1 + (t2**2)
    t1 = t2
    t2 = result
print (result)
