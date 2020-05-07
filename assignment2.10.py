class minimum:
    
    def __init__(self):
        self.x=int(input("5 rupaye ke sikke?"))
        self.y=int(input("1 rupaye ke sikke?"))
        self.price=int(input("kitne dene hai?"))
        self.calculator()

    def calculator(self):
        if self.price%5==0:
            print("no. of 5 ruppee coins are",self.price//5)
        else:
            n1=self.price//5
            n2=self.price%5

            if n1<=self.x and n2<=self.y:
                print("5 ruppee coins are--->",n1,"\n1 ruppee coins are--->",n2)
            else:
                print("exact change isn't available")
            
