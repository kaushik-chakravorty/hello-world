from tkinter import*
import requests

class Irctc:
    def __init__(self):#without self no object will be created and hence the code will not run as class can be accessed only by it's objects
        self.root=Tk()
        self.root.title("IRCTC")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#0023ae")
        #self.root is the main thing, consider it as the screen
        #geometry manager is the interior designer
        self.label1=Label(self.root,text="Train Route",bg="#F9250E",fg="#ffffff")
        self.label1.configure(font=("constantia",22,"bold"))
        self.label1.pack(pady=(30,10))#upar se 30 chor ke aayega niche se 10 chor ke ayega

        self.trainNo=Entry(self.root)#enters a text box
        self.trainNo.pack(ipadx=45,ipady=10)#sets the size of text box



        click=Button(self.root,text="Fetch Stations",width=30,height=2,command=lambda:self.fetch())#button is a class which acts as a button
        click.pack(pady=(15,15))


        self.result=Label(self.root,bg="#F9250E",fg="#ffffff")
        self.result.configure(font=("constantia",12,))
        self.label1.pack(pady=(5,10))#upar se 30 chor ke aayega niche se 10 chor ke ayega



        self.root.mainloop()

    def fetch(self):
        trainNo=self.trainNo.get()
        print(trainNo)
        url="https://api.railwayapi.com/v2/route/train/{}/apikey/4aptnety30".format(trainNo)
        response=requests.get(url)#thiss is get() function of requests apart from that of tkinter
        data=response.json()#tells python the data is in json format
        print(data)


        for i in data['route']:
            
            stations=stations+i['station']['name']+ "  "+i['scharr']+"  "+i['schdep']+"   "+str(i[distance])+"km" + "\n"
        self.result.configure(text=stations)

obj=Irctc()
