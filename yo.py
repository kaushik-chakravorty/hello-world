class ATM:


    pin=""
    balance=0
    __counter=1001


    def create_pin(self):
        self.pin=input("set ATM pin")
        print("pin setup sucessful")
        print("acc no",self.accno)
        atm.__counter=atm.__counter+1

    @staticmethod#decorator-gives special meanings to objects

    def get_counter():#counter can be accessed even if obj is not created
        return atm.__counter

    def deposit(self):
        temp=input("enter your pin")
        if self.pin==temp:
            amount=input("enter amount to be deposited")
            self.balance=self.balance+amount
            print("deposit successful")
        else:
            print("incorrect pin")

    def withdraw(self):
        temp=input("enter your pin")
        if self.pin==temp:
            amount=input("enter amount to be withdrawn")
            if amount<self.balance:
                self.balance=self.balance-amount
            
            else:
                print("insufficient funds")
                
        
        else:
            print("incorrect pin")
        c=str(input("display balance? enter y for yes and n for no"))
        if c=="y":
            print("balance=",self.balance)
    def checkBalance(self):
        temp=input("enter your pin")
        if self.pin==temp:
            print("account balance= ",self.balance)
        
        else:
            print("incorrect pin")

    def change_pin(self):
        temp=input("enter previous pin")
        if self.pin==temp:
            self.pin=input("enter new pin")

        else:
            print("incorrect pin")

            
