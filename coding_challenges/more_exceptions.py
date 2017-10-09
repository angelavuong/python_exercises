'''

Name: More Exceptions

Input: Write a Calculator class with a single method: int power(int, int)
The power method takes two integers, n and p, as parameters and returns the integer result of n**p.
If either n or p is negative, then the method must throw an exception with the message:
'n and p should be non-negative'

Sample Input:
4
3 5
2 4
-1 -2
-1 3

Sample Output:
243
16
n and p should be non-negative
n and p should be non-negative
'''

class Calculator(object):
    def power(self, n, p):
        self.n = n
        self.p = p
        if(n >= 0 and p >= 0):
            total = n ** p
            return total
        else:
            return 'n and p should be non-negative'

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
