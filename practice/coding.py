l=[0,0]
n=input("enter string for movement")
for i in range(len(n)):
    if n[i]=='R':
        l[0]=l[0]+1
    elif n[i]=='L':
        l[0]=l[0]-1
    elif n[i]=='U':
        l[1]=l[1]+1
    elif n[i]=='D':
        l[1]=l[1]-1

    else:
        print("inputs should be either R(right),L(left),U(up),D(down)")
if l==[0,0]:
    print("True")

else:
    print("False")
