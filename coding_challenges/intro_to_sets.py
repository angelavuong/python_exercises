'''

Name: Introduction to Sets

Sets: A set is an unordered collection of elements without duplicate entries.

Task:
Average = Sum of Heights / Total Number of Heights

Sample Input:
10
161 182 161 154 176 170 167 171 170 174

Sample Output:
169.375

'''

def average(array):
    z = set(array)
    total = sum(z)/len(z)
    return total


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
