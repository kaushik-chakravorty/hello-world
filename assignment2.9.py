class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Stack:
    def __init__(self):
        self.top=None
        self.elements=0

    def input(self,data):
        node=Node(data)
        if self.elements==0:
            self.top=node

        else:
            node.next=self.top
            self.top=node

        self.elements+=1

    def traverse(self):
        temp=self.top
        while temp is not None:
            print(temp.data)
            temp=temp.next

    def calculator(self):
        
        if self.top.data==7:
            self.top=self.top.next

        temp=self.top
        self.result=1
        while temp is not None:
            if temp.data==7:
                if temp.next is None:
                    self.result=-1
                else:
                    self.result=1
                    self.result=self.result*temp.next.data
                    return self.result
                                        
                                    
                                    
                                
                                
                                
            else:
                self.result=self.result*temp.data
            temp=temp.next
        return self.result

                        






s=Stack()
s.input(4)
s.input(2)
s.input(2)
s.input(7)
s.traverse()
a=s.calculator()
print(a)


        
        
