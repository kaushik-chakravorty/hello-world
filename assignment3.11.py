class leap:
    def __init__(self):
        self.year=int(input("year baap dega bhinchod tmhara"))
        self.leap()


    def leap(self):
        l=[]
        while len(l)!=15:
            if self.year%100==0:
                if self.year%400==0:
                    l.append(self.year)
                else:
                    pass

            
                
                    



            elif self.year%4==0:
                l.append(self.year)

            else:
                pass

                print(self.year,"----> discarded data")
            self.year+=1
        print(l)

s=leap()

  

