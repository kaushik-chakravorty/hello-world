from abc import ABC, abstractmethod#abstract classes
class product(ABC):
    @abstractmethod#without implementing this method in some otheer class inheritance of this abtract class doesn't happen 
    def return_policy():
        pass
class Furniture(product):
    def hello(self):
        print("hello")
    def returnPolicy():
        pass
obj=Furniture()
