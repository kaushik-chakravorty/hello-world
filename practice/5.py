a=int(input("ente rthe amount"))
b=a%5


if a%10==0:
    q=a//5
    print("result=",q)
else:
    if b==1:
        x=(a//5)
        y=x+1
        print( "5 rupee coions are  ",x, "1 rupee coins are 1")
    if b==2:
        x=(a//5)
        y=x+1
        print( "5 rupee",x, "2 rupee coins are 1", )
    if b==3:
        x=(a//5)
        y=x+2
        print("5 rupee",x,  "2 rupee coins are 1 and 1 ruppee 1")
    if b==4:
        x=(a//5)
        y=x+2
        print("5 rupee",x, "2 rupee coins are 2")
        
