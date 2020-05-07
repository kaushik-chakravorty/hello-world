l_perfect=[]
for i in range(1,10001):
    l=[]
    for j in range(1,i):
        if i%j==0:
            l.append(j)
    if sum(l)==i:
        l_perfect.append(i)
print('perfect numbers are\n',l_perfect)

        
