'''
Name: Review Loop

Task:
Given a string, S, of length, N, that is index, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.

Input:
The first line contains an integer, N, (number of test cases)
Each line i contains string S

Output:
Print even-indexed followed by odd-indexed


Sample Input:
2
Hacker
Rank

Sample Output:
Hce akr
Rn ak
'''

if __name__ == '__main__':
    a = []
    even = []
    odd = []
    lst = []
    n = int(input().strip()) # Number of sites
    for i in range(n):
        s = input().strip()
        lst.append(s)

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if(j%2==1):
                odd.append(lst[i][j])
            elif(j%2==0):
                even.append(lst[i][j])
        print(''.join(str(x) for x in even) +" " + ''.join(str(x) for x in odd))
        even = []
        odd = []
