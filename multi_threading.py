import time,threading#threading is a module which contains all the functionalities 
def sq(l):

     for i in l:
         time.sleep(0.5)
         print(i**2)

def cube(l):


    for i in l:
        time.sleep(0.5)
        print(i**3)
l=[1,2,3,4,5,6,7,8,9]

start=time.time()
t1=threading.Thread(target=sq,args=(l,))
t2=threading.Thread(target=cube,args=(l,))
t1.start()
t2.start()
t1.join()
t2.join()
#sq(l)
#cube(l)
print(time.time()-start)
