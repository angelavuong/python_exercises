'''

Name: Palindrome

Task: A palindrome is a word, phrase, number, or other sequence of characters which
reads the same backwards and forwards. Can you determine if a given string, s, is a palindrome?

Sample Input:
racecar

Sample Output:
The word, racecar, is a palindrome.

'''


import sys

class Solution:
    def __init__(self):
        self.stack = list()
        self.queue = list()
        return (None)

    # Write your code here
    def pushCharacter(self,s):
        self.stack.append(s)
    def enqueueCharacter(self,s):
        self.queue.append(s)
    def popCharacter(self):
        return self.stack.pop(-1) #top of the stack
    def dequeueCharacter(self):
        return self.queue.pop(0) #first character in queue

# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
