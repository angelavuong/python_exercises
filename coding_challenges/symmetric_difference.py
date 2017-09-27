'''
Name: Symmetric Difference

Task:
Given two integers, M and N, print their symmetric difference in ascending order.

Input:
First line = integer M
Second line = M space-separated integers
Third line = integer N
Fourth line = N space-separated integers

Sample Input:
4
2 4 5 9
4
2 4 11 12

Sample Output:
5
9
11
12

'''

difference = []
complete_list = []
n1 = int(input().strip())
m = set(map(int, input().split()))
n2 = int(input().strip())
n = set(map(int, input().split()))

difference = m.intersection(n)
for each in m:
    if(each not in difference):
        complete_list.append(each)
for each in n:
    if(each not in difference):
        complete_list.append(each)
complete_list = sorted(complete_list)
for i in range(len(complete_list)):
    print (complete_list[i])
