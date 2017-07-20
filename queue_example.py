#Queue Example
from Queue import Queue
import sys

queue = ["Wake up", "Have a coffee", "Have a shower", "Get dressed", "Have breakfast"]

def view():
    for x in range(len(queue)):
        print(queue[x])

def push():
    item = raw_input("Please enter the item you wish to add to the queue: ")
    queue.append(item)

def pop():
    item = queue.pop(0) #pops first item out of list
    print('You just popped out:', item)


while True:

    print("")
    print ("Python Implementation of a Queue")
    print ("1. View Queue")
    print ("2. Push onto Queue")
    print ("3. Pop out of Queue")
    print ("4. Exit")
    print("")
    menu_choice = int(input("Please enter your menu choice: "))

    if menu_choice == 1:
        view()

    if menu_choice == 2:
        push()

    if menu_choice == 3:
        pop()

    if menu_choice == 4:
        quit()
