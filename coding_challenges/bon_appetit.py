'''
Name: Bon Appetit

Task:
Anna and Brian order n items at a restaurant, but Anna declines to eat any of the kth item (where 0 <= k <= n) due to
an allergy. When the check comes, they decide to spit the cost of all the items they shared; however, Brian may have forgotten
that they didn't split the kth item and accidentally charged Anna for it.

Input:
The first line contains two space-separated integers denoting the respective values of n (number of items ordered) and k(the 0-based index of the item that
Anna did not eat)
The second line contains n space-separated integers where each integer i denotes the cost, c[i], of item i
The third line contains an integer, b-charged, denoting the amount of money that Brian charged Anna for her share of the bill.

Output:
You are given n, k, the cost of each of the n items, and the total amount of money that Brian charged Anna for her portion
of the bill. If the bill is fairly split, print Bon Appetit; otherwise, print the amount of money that Brian must refund to Anna.
'''
#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    total = 0
    for i in range(n):
        if(i != k):
            total = total + ar[i]
        else:
            pass
    shared_amount = total/2
    if(shared_amount == b):
        return 'Bon Appetit'
    else:
        return int(b - shared_amount)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
