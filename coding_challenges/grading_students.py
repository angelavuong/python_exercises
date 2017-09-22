'''
Name: Grading Students
Task:
- If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
- If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Example:
grade = 84 will be rounded to 85
grade = 29 will not be rounded because it is less than 40
'''

#!/bin/python3
import sys

def solve(grades):
    # Complete this function
    new_list = []
    for each in grades:
        if (each < 38):
            pass
        else:
            if (each%5 >= 3):
                remainder = 5 - (each%5)
                each = remainder + each
            elif(each%5 == 0):
                pass
            else:
                pass
        new_list.append(each)
    return new_list

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
