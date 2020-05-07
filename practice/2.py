l=[1,34,56,87,54]
n=len(l)
a=int(input("enter the nth largest no"))
#if a<n:
for i in range(0,n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l[a-1])

                
            
            
