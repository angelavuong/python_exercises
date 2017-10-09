'''

Name: Linked List

Tasks: Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and insert
it at the tail of the linked list referenced by teh head parameter. Once the new node is added, return the reference to the head node.


Sample Input:
4
2
3
4
1

Sample Output:
2 3 4 1
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data):
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
