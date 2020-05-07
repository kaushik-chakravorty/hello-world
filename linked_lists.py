#linked lists#aggregation is used to create a linked list

class Node:


    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,node):
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=self.tail.next
            self.tail.next=None
    def display(self):
        l=[]
        temp=self.head
        while temp is not None:
            l.append(temp.data)
            temp=temp.next

        print(l)
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)

            
            
