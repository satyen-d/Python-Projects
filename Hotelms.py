class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):
        print ("\n\n----- WELCOME TO CFC HOTEL -----\n - By Satyen Deshpande\n")
        self.rt=rt
        self.r=r
        self.t=t
        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno

    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")
        
    def roomrent(self):
        while(1):
            print ("We have the following rooms for you:-")
            print ("1.  Type A = Rs 6000/-")
            print ("2.  Type B = Rs 5000/-")
            print ("3.  Type C = Rs 4000/-")
            print ("4.  Type D = Rs 3000/-")
            print ("5.  Exit")
            x=int(input("Enter Your Choice Please->\t"))
            n=int(input("For How Many Nights Did You Stay:\t"))

            if(x==1):
                print ("you have opted room type A")
                self.s=6000*n
                print ("your room rent is =",self.s,"\n")
                break
            elif (x==2):
                print ("you have opted room type B")
                self.s=5000*n
                print ("your room rent is =",self.s,"\n")
                break
            elif (x==3):
                print ("you have opted room type C")
                self.s=4000*n
                print ("your room rent is =",self.s,"\n")
                break
            elif (x==4):
                print ("you have opted room type D")
                self.s=3000*n
                print ("your room rent is =",self.s,"\n")
                break
            elif (x==5):
                break
            else:
                print ("Invalid option")


    def restaurentbill(self):
        print("---- RESTAURANT MENU ----")
        print("1.water----->Rs20 \n","2.tea----->Rs10 \n","3.breakfast combo--->Rs90 \n","4.lunch---->Rs110 \n","5.dinner--->Rs150 \n","6.Exit")

        while (1):
            c=int(input("Enter your choice:\t"))

            if (c==1):
                d=int(input("Enter the quantity:\t"))
                self.r=self.r+20*d
            elif (c==2):
                 d=int(input("Enter the quantity:\t"))
                 self.r=self.r+10*d
            elif (c==3):
                 d=int(input("Enter the quantity:\t"))
                 self.r=self.r+90*d
            elif (c==4):
                 d=int(input("Enter the quantity:\t"))
                 self.r=self.r+110*d
            elif (c==5):
                 d=int(input("Enter the quantity:\t"))
                 self.r=self.r+150*d
            elif (c==6):
                break;
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.r,"\n")


    def	laundrybill(self):
        print ("---- LAUNDRY MENU ----")
        print ("1.Shorts----->Rs3\n","2.Trousers----->Rs4\n","3.Shirt--->Rs5\n","4.Jeans---->Rs6\n","5.Girlsuit--->Rs8\n","6.Exit")

        while (1):
            e=int(input("Enter your choice:\t"))

            if (e==1):
                f=int(input("Enter the quantity:\t"))
                self.t=self.t+3*f
            elif (e==2):
                f=int(input("Enter the quantity:\t"))
                self.t=self.t+4*f
            elif (e==3):
                f=int(input("Enter the quantity:\t"))
                self.t=self.t+5*f
            elif (e==4):
                f=int(input("Enter the quantity:\t"))
                self.t=self.t+6*f
            elif (e==5):
                f=int(input("Enter the quantity:\t"))
                self.t=self.t+8*f
            elif (e==6):
                break;
            else:
                print ("Invalid option")

        print ("Total Laundary Cost=Rs",self.t,"\n")


    def gamebill(self):
        print ("---- GAME MENU ----")
        print ("1.Table tennis----->Rs60\n","2.Bowling----->Rs80\n","3.Snooker--->Rs70\n","4.Video games---->Rs90\n","5.Pool--->Rs50==6\n","6.Exit")

        while (1):
            g=int(input("Enter your choice:\t"))

            if (g==1):
                h=int(input("No. of hours:\t"))
                self.p=self.p+60*h
            elif (g==2):
                h=int(input("No. of hours:\t"))
                self.p=self.p+80*h
            elif (g==3):
                h=int(input("No. of hours:\t"))
                self.p=self.p+70*h
            elif (g==4):
                h=int(input("No. of hours:"))
                self.p=self.p+90*h
            elif (g==5):
                h=int(input("No. of hours:\t"))
                self.p=self.p+50*h
            elif (g==6):
                break;
            else:
                print ("Invalid option")

        print ("Total Game Bill=Rs",self.p,"\n")


    def display(self):
        print ("---- HOTEL BILL ----")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
        print ("Your laundary bill is:",self.t)
        print ("Your Game bill is:",self.p)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1


def main():
    a=hotelfarecal()
    
    while (1):
        print("1.Enter Customer Data")
        print("2.Calculate Room Rent")
        print("3.Calculate Restaurant Bill")
        print("4.Calculate Laundry Bill")
        print("5.Calculate Gaming Bill")
        print("6.Show Total Cost")
        print("7.EXIT")
        b=int(input("\nEnter your choice:\t"))

        if (b==1):
            a.inputdata()
        if (b==2):
            a.roomrent()
        if (b==3):
            a.restaurentbill()
        if (b==4):
            a.laundrybill()
        if (b==5):
            a.gamebill()
        if (b==6):
            a.display()
        if (b==7):
            quit()

main()

