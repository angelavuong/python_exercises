'''

Name: Disjoint Sets

Task:
For each i integer in the array, if A is in array, happy +1, else B in array, happy -1.

Input Format:
First line = n (size of n array) and m (size of A and B arrays)
Second line = n integer
Third line = A (what she likes)
Fourth line = B (what she dislikes)

Sample Input:
3 2
1 5 3
3 1
5 7

Sample Output:
1
'''

n,m = input().split()
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print (sum([(i in a) - (i in b) for i in arr]))
