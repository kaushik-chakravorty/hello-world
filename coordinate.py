class coor:
    def __init__(self):
         x=int(input("enter x coordinate"))
         y=int(input("enter y coordinate"))
         print("co-ordinate is ({},{})".format(x,y))
    def dfo(self,x,y):
        d=((x**2)+(y**2))**0.5
        print(d)
    def dbtp(self,a,b):
        d=(((a[0]-b[0])**2)+((a[1]-b[1])**2))**0.5
        print(d)
    def eqn(self,a,b):
        m=(a[1]-b[1])/(a[0]-b[0])
        print("equation will be y={}x+{}".format(m,(a[1]-a[0]*m)))
    def midpoint(self,a,b):
         m=(a[1]-b[1])/(a[0]-b[0])
        if()
