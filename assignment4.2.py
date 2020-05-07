

def joiner(l):
    d={}
    l2=[]
    for i in l:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1

    for i in d.keys():
        l2.append(i)
    return l2
    



def run_length(s):
    
    l=[]
    count1=0
    for i in range(len(s)):
        count=1
        
        for j in range(len(s)):
            if s[i]==s[j] and j!=i:
                count+=1
                
        x='{}'.format(count)+'{}'.format(s[i])
        
        l.append(x)
        l1=joiner(l)


    return l1

s=input("enter the string")
l=run_length(s)
print("".join(l))
            
