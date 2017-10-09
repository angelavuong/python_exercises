'''

Name: Scope

Tasks: Complete the Difference class by writing the following:
- A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
- A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.

|1-2| = 1
|1-5| = 4
|2-5| = 3

Sample Input:
3
1 2 5

Sample Output:
4
'''

class Difference:
    def __init__(self, a):
        self.__elements = a
    	# Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        for i in range(len(a)):
            for j in range(len(a)):
                if(i != j):
                    if(abs(a[i] - a[j]) > self.maximumDifference):
                        self.maximumDifference = abs(a[i] - a[j])
                    else:
                        pass
        return self.maximumDifference
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
