'''

Name: Abstract Classes

Tasks: Given a Book class and a Solution class, write a MyBook class that does the following:
- Inherit from Book
- Has a parameterized constructor taking these 3 parameters:
  1. String: title
  2. String: author
  3. Int: price
- Implements the Book class' abstract display() mehod so it prints these 3 lines:
  1. Title: a space and then the current instance's title
  2. Author: a space and then the current instance's author
  3. Price: a space and then the current instance's price


Sample Input:
The Alchemist
Paulo Coelho
248

Sample Output:
Title: The Alchemist
Author: Paulo Coelho
Price: 248
'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print('Title: ' + self.title)
        print('Author: ' + self.author)
        print('Price: ' + str(self.price))

title=input() 
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
