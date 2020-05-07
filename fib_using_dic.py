#dynamic programming
def fib(n,d):
    if n in d:
        return d[n]
    else:
        value=fib(n-1,d)+fib(n-2,d)
        d[n]=value
        return  value
d={0:1,1:1}
print(fib(991,d))
