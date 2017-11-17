#!/bin/python3

import sys

def ask_function(A,command):
    i = int(command[1]) - 1
    j = int(command[2]) - 1
    k = int(command[3]) - 1
    l = int(command[4]) - 1
    m = int(command[5])
    num_product = 1
    den_product = 1

    # p(i,j)
    for i in range(i,A[j]):
        num_product = num_product * A[i]
    # p(k,l)
    if(k == l):
        den_product = A[k]
    else:
        for k in range(k,A[l]):
            den_product = den_product * A[k]
    total = num_product/den_product
    if (total >= 1):
        modulo = total % m
        return int(modulo)
    else:
        return -1


if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    q = int(input().strip())
    for a0 in range(q):
        # Write Your Code Here
        command = input().strip().split(' ')
        if(command[0] == '2'): # Ask
            print(ask_function(A,command))
        elif(command[0] == '1'): # Set
            value_start = int(command[1]) - 1
            value_end = int(command[2]) - 1
            for i in range(A[value_start]-1,A[value_end]):
                A[i] = int(command[3])


      
