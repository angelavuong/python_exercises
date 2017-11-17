#!/bin/python3

import sys

def productOfPages(a, b, c, d, p, q):
    # Return the product of the page counts of the missing books
        if(p == a): a = 1
        elif(p == b): b = 1
        elif(p == c): c = 1
        elif(p == d): d = 1

        if(q == a): a = 1
        elif(q == b): b = 1
        elif(q == c): c = 1
        elif(q == d): d = 1

        product = a * b * c * d
        return product

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        a, b, c, d = input().strip().split(' ')
        a, b, c, d = [int(a), int(b), int(c), int(d)]
        p, q = input().strip().split(' ')
        p, q = [int(p), int(q)]
        answer = productOfPages(a, b, c, d, p, q)
        print(answer)
