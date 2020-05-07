#objects of class Node are added(using add method in LL class) to the LL class(nodes are added to the linked list) which shows use of aggregation 
l=[2,6,3,5,8,9]
l_node=[]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_list(self,l_temp):##if multiple objects of Node class(nodes) have to be added to LL class(linked list) at once
        for i in range(0,len(l_temp)):
            
            self.add(l_temp[i])
        



    def add(self,node):
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=self.tail.next
            self.tail.next=None
    def xseries(self):
        self.l=[]
        temp=self.head
        while (temp.next).next is not None:
            if (temp.data+temp.next.data)==(temp.next).next.data:
                self.l.append([temp.data,temp.next.data])
                temp=temp.next
            else:
                temp=temp.next
        print(self.l)
    def display(self):
        l1=[]
        temp=self.head
        while temp is not None:
            l1.append(temp.data)
            temp=temp.next
        print(l1)

    def longestxseries(self):#can be invoked only after the method xseries has been used
        for i in range(0,len(self.l)-1):
            if len[l[i]]<len([l[i]]):
                a=l[i]
        print(a)
for i in range(0,len(l)):
    l_node.append(Node(l[i]))#makes a list comprising of objects of Node class(nodes)
ll=LL()
ll.add_list(l_node)
ll.xseries()



    



    
                
                
            
