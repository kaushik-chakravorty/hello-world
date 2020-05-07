import ctypes
class Mlist:
    def __init__(self):
        self.capacity=1#maximum length of array
        self.number=0#how many numbers are there
        self.A=self.make_array(self.capacity)


    def __str__(self):
        result=""

        for i in range(self.number):
            result=result+str(self.A[i])+","
        return "[{}]".format(result[:-1])

    def __len__(self):
        return self.number
    




    def __getitem__(self,index):
        return self.A[index]

    def append(self,value):
        if self.number==self.capacity:
            self.resize(2*self.capacity)#forms a new array of double capacity

        self.A[self.number]=value

        self.number+=1
            
    def insert(self,index,value):
         if self.number==self.capacity:
            self.resize(2*self.capacity)#forms a new array of double capacity


         for i in range(self.number,index,-1):
    
            self.A[i]=self.A[i-1]#backward loop creates an empty value at i=index and it is addded outside loop
         self.A[index]=value

         self.number+=1            
         


    def pop(self,index):
        if index>self.number:
            print("index error")
        else:
            print("no popped out is", self.A[index])
        

        
    def delete(self,index):
        for i in range(index,self.number-1):
            self.A[i]=self.A[i+1]
        self.number-=1


    def resize(self,new_capacity):
        B=self.make_array(new_capacity)

        for i in range(0,self.number):
            B[i]=self.A[i]
        self.A=B
        self.capacity=new_capacity

    def make_array(self,capacity):
        return(capacity*ctypes.py_object)()
        
