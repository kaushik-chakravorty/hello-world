def side(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        print("chalega boss")
    else:
        print("na ho paayega")

l=[]
for i in range(0,3):
    x=int(input("enter length of side {}".format(i+1)))
    l.append(x)

side(l[0],l[1],l[2])

    
    
