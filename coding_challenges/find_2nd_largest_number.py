'''
Name: Find the 2nd Largest Number

Task:
You are given n numbers. Store them in a list and find the second largest number.

Input:
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Output:
Print the value of the second largest number.
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_value = arr[0]

    for i in range(n):
        if (arr[i] > max_value):
            max_value = arr[i]
        else:
            pass
    for i in range(n):
        if (arr[i] == max_value):
            arr[i] = -100

    max_value = arr[0]
    for i in range(n):
        if (arr[i] > max_value):
            max_value = arr[i]
    print (max_value)
