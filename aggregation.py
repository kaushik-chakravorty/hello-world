class customer:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age)
        print(self.address.get_city())

class address:
    def __init__(self,pin,city):
        self.__pin=pin
        self.__city=city
    def get_city(self):
        return (self.__city,self.__pin)
        #return self.__pin
add1=address(70001,"patna")
cust=customer('kaushik',34,add1)
