'''
Name: Class vs Instance

Task:
Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. The constructor must assign initialAge
to age after confirming the argument passed as initialAge is not negative; if a negative argument is passed as initialAge, the constructor should set up age to 0
and print 'Age is not valid, setting age to 0'. In addition, you must write the following instance methods:
1. yearPasses() should increase the age instance variable to 1
2. amIOld() should perform the following conditional actions:
- if age < 13: print 'You are young'
- if age >= 13 and age < 18: print 'You are a teenager'
- otherwise, print 'You are old'

Input:
First line contains integer, T (number of test cases), and the T subsequent lines each contain an integer denoting the age of the Person instance.

Output:
Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your
methods are implemented correctly, each test case will print 2 or 3 lines (depending on whether or not a valid initialAge was passed to the constructor)
'''

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if (initialAge < 0):
            initialAge = 0
            print ('Age is not valid, setting age to 0.')

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if(self.initialAge < 13):
            print('You are young.')
        elif(self.initialAge >= 13 and self.initialAge < 18):
            print ('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge += 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
