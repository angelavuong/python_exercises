'''

Name: .add()

Task:
Find total number of distinct country stamps.

Sample Input:
7
UK
China
USA
France
New Zealand
UK
France

Sample Output:
5
'''
n = int(input().strip())
lst = []
for _ in range(n):
    name = input()
    lst.append(name)
count = len(set(lst))
print(count)
