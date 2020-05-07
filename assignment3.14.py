def calculator():
    heads=int(input("enter no of heads"))
    legs=int(input("enter no of legs"))
    x=0
    y=heads
    c=0
    while x<=heads:
        if 4*x+2*y==legs:
            print("rabbits--->",x, "\n chickens--->",y)
            c=1
            return
        else:
            x+=1
            y-=1


    if c==0:
        print("not possible")


calculator()
