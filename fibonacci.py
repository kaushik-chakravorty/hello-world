import time
def fib(m):
    d={0:1,1:1}
    
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1)+fib(m-2)
    

start=time.time()
print(fib(38))
print(time.time()-start,"secs")
