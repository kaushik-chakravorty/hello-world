l=[[1,2,3],[4,5,6],[7,8,9]]
#l=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
l1=[]
n=len(l)
print(n)

for i in range(0,n):
    if i==0:
        
        for j in range(0,n):
            
                l1.append(l[i][j])

    else:
         
         
        l1.append(l[i][n-1])
       
print(l1)

for i in range(n-1,0,-1):
    for j in range(n-2,-1,-1):
        l1.append(l[i][j])
l1[-2],l1[-1]=l1[-1],l1[-2]
print(l1)
