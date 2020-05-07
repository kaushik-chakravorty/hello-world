#a=int(input("how many units to right?"))
#b=int(input("how many units to left?"))
#c=int(input("how many units to top?"))
#d=int(input("how many units to bottom?"))
x=[0,0]
for i in range(0,4):
    a=input("enter input")
    l=a.split()
if l[0]=="R":
    x[0]=x[0]+int(l[1])
if l[0]=="L":
    x[0]=x[0]-int(l[1])
if l[0]=="T":
    x[1]=x[1]+int(l[1])
if l[0]=="B":
    x[1]=x[1]-int(l[1]) 
y=tuple(x)
print("final co ordinate will be",y)
