class Student:
    def __init__(self,branch,score):
        self.branch=branch
        self.score=score



    def detScho(self):
        self.scholarship=0
        if self.branch=="arts":
            if self.score>=90:
                self.scholarship=50
            else:
                if self.score%2!=0:
                    self.scholarship=5
                else:
                    self.scholarship=0
        elif self.branch=="engineering":
             
                if self.score>85:
                    self.scholarship=50
                elif self.score%7==0:
                    self.scholarship=5
                else:
                    print("no self.scholarship anna")
        else:
            print("invalid branch")
        print("the self.scholarship %age is",self.scholarship,"%")
        


    def fees(self,cf):
        if self.scholarship==0:
            print("full payment must be done")
        else:
        
            ffees=cf-((cf*self.scholarship)/100)
            print("fees to be paid is",ffees)
            
        


        
student=Student("engineering",34)
student.detScho()
student.fees(50000)
            
            
