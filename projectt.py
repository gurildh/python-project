from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import random
import time
import datetime

root=Tk()
root.geometry("1880x750")
root.title("Train Ticket")
root.configure(background="black")

##----------------------Declaring variables-----------------##

text_input=StringVar()
operator=("")
Tax =StringVar()
SubTotal =StringVar()
TotalCost=StringVar()
Total=StringVar()
date1=StringVar()
time1=StringVar()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
Tax=StringVar()

TicketClass=StringVar()
TicketPrice=StringVar()
Child_Ticket=StringVar()
Adult_Ticket=StringVar()
From_Destination=StringVar()
To_Destination=StringVar()
Fee_Price=StringVar()
Route=StringVar()
Receipt_Ref=StringVar()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("")
var8.set("")
var9.set("")
var10.set("0")
var11.set("0")
var12.set("")
Tax.set("")
Total.set("")
SubTotal.set("")
TotalCost.set("")
TicketClass.set("")
TicketPrice.set("")
Child_Ticket.set("")
Adult_Ticket.set("")
From_Destination.set("")
To_Destination.set("")
Fee_Price.set("")
Route.set("")
Receipt_Ref.set("")


##---------------------Functions----------------------##

def Click(numbers):
    global operator
    operator = operator +str(numbers)
    text_input.set(operator)

def Clear():
    global operator
    operator=""
    text_input.set("")

def equal():
    global operator
    sumup =str(eval(operator))
    text_input.set(sumup)
    operator("")

def Exitt():
    qExit= messagebox.askyesno("Quit System","Do you want to quit?")
    if qExit>0:
        root.destroy()
        return

def reset():
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("")
    var8.set("")
    var9.set("")
    var10.set("0")
    var11.set("0")
    var12.set("")

    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Fee_Price.set("")
    TicketClass.set("")
    Total.set("")
    TicketPrice.set("")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    From_Destination.set("")
    To_Destination.set("")
    Fee_Price.set("")
    Route.set("")
    Receipt_Ref.set("")

#Date and Time
date1.set(time.strftime("%d/%m/%y"))
time1.set(time.strftime('%H:%M:%S'))

def Travel_Cost():
    if (var9.get()=="Pathankot" and  var4.get()== 1):
        if (var1.get()== 1):
            Tcost = float(600)
            TicketClass.set("Standard")
        elif(var2.get()==1):
            Tcost = float(280)
            TicketClass.set("Economy")
        elif(var3.get()==1):
            Tcost = float(800)
            TicketClass.set("First_Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))

        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Ludhiana")
        To_Destination.set("Pathankot")
        Fee_Price.set(TotalCost)
        Total.set(Adult_Fees)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)

    elif (var9.get()=="Pathankot" and var5.get()==1):
        if (var1.get() == 1):
            Tcost = float(500)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(200)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
                Tcost = float(600)
                TicketClass.set("First_Class")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Ludhiana")
        To_Destination.set("Pathankot")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)

    elif (var9.get()== "Chandigarh" and var4.get()== 1):
        if(var1.get()== 1):
            Tcost = float(100)
            TicketClass.set("Standard")
        elif(var2.get()==1):
            Tcost = float(50)
            TicketClass.set("Economy")
        elif(var3.get()==1):
            Tcost = float(305)
            TicketClass.set("First_Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Ludhiana")
        To_Destination.set("Chandigarh")
        Fee_Price.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Chandigarh" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(100)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(30)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
                Tcost = float(200)
                Single = float(var12.get())
                TicketClass.set("First_Class")
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Ludhiana")
        To_Destination.set("Chandigarh")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)

    elif (var9.get()== "Amritsar" and var4.get()== 1):
        if (var1.get()== 1):
            Tcost = float(754)
            TicketClass.set("Standard")
        elif(var2.get()==1):
            Tcost = float(50)
            TicketClass.set("Economy")
        elif(var3.get()==1):
            Tcost = float(1245)
            TicketClass.set("First_Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Ludhiana")
        To_Destination.set("Amritsar")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Amritsar" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(660)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(30)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
                Tcost = float(800)
                TicketClass.set("First_Class")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Ludhiana")
        To_Destination.set("Amritsar")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)

    elif (var9.get()== "Patiala" and var4.get()== 1):
        if (var1.get()== 1):
            Tcost = float(495)
            TicketClass.set("Standard")
        elif(var2.get()==1):
            Tcost = float(140)
            Single = float(var12.get())
            TicketClass.set("Economy")
        elif(var3.get()==1):
            Tcost = float(700)
            TicketClass.set("First_Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Ludhiana")
        To_Destination.set("Patiala")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Patiala" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(390)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(75)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
                Tcost = float(565)
                TicketClass.set("First_Class")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Ludhiana")
        To_Destination.set("Patiala")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)

    elif (var9.get()== "Chennai" and var4.get()== 1):
        if (var1.get()== 1):
            Tcost = float(2000)
            TicketClass.set("Standard")
        elif(var2.get()==1):
            Tcost = float(1053)
            TicketClass.set("Economy")
        elif(var3.get()==1):
            Tcost = float(3000)
            TicketClass.set("First_Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Ludhiana")
        To_Destination.set("Chennai")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Chennai" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(1600)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(880)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
                Tcost = float(2090)
                TicketClass.set("First_Class")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Ludhiana")
        To_Destination.set("Chennai")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)

    elif (var9.get()== "Delhi" and var4.get()== 1):
        if (var1.get()== 1):
            Tcost = float(1385)
            TicketClass.set("Standard")
        elif(var2.get()==1):
            Tcost = float(210)
            TicketClass.set("Economy")
        elif(var3.get()==1):
            Tcost = float(1605)
            TicketClass.set("First_Class")
        Single = float(var12.get())
        Adult_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Adult_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Adult_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Adult_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Ludhiana")
        To_Destination.set("Delhii")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


    elif (var9.get()== "Delhi" and var5.get()== 1):
        if (var1.get() == 1):
            Tcost = float(780)
            TicketClass.set("Standard")
        elif (var2.get() == 1):
            Tcost = float(150)
            TicketClass.set("Economy")
        elif (var3.get() == 1):
                Tcost = float(1000)
                TicketClass.set("First_Class")
        Single = float(var12.get())
        Child_Tax = "₹", str('%.2f' % ((Tcost * Single) * 0.05))
        Child_Fees = "₹", str('%.2f' % (Tcost * Single))
        TotalCost = "₹", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.05)))
        if (var11.get() == 1):
            Single = float(var12.get())
            Child_Tax = "₹", str('%.2f' % (((Tcost * Single) * 0.05)*2))
            Child_Fees = "₹", str('%.2f' % ((Tcost * Single)*2))
            TotalCost = "₹", str('%.2f' % (((Tcost * Single) + ((Tcost * Single) * 0.05))*2))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Ludhiana")
        To_Destination.set("Delhi")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109,5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)


##-----------------Root frames coding------------------##
top=Frame(root, width=1920, height=200,bd=8,relief="raise")
top.pack(side=TOP,fill=X)
f1=Frame(root, width=1000, height=710,bd=8,relief="raise")
f1.pack(side=LEFT, fill=Y)
f2=Frame(root, width=520, height=710,bd=8,relief="raise")
f2.pack(side=RIGHT, fill=Y)

##------------------Top Frame coding-------------------##
toplabel=Label(top,text="Train Ticketing System",font=("times",32,"bold"))
toplabel.pack()

##--------------------------Left Top coding-------------##
f1a=Frame(f1, width=970, height=300,bd=8,relief="raise")
f1a.pack(side=TOP,fill=X)

##-----First Box Coding------##
topleft1=Frame(f1a, width=310, height=300,bd=8,relief="raise")
topleft1.pack(side=LEFT,fill=Y)

leftlabel=Label(topleft1,text="Class",font=("times",40,"bold"))
leftlabel.pack()
leftcheck1=Checkbutton(topleft1,text="Standard",font=("times",32),onvalue=1,offvalue=0,variable=var1)
leftcheck1.pack()
leftcheck2=Checkbutton(topleft1,text="Economy",font=("times",32),onvalue=1,offvalue=0,variable=var2)
leftcheck2.pack()
leftcheck3=Checkbutton(topleft1,text="First Class",font=("times",30),onvalue=1,offvalue=0,variable=var3)
leftcheck3.pack()

##--------------Second Box Coding---------##
topleft2=Frame(f1a, width=410, height=300,bd=8,relief="raise")
topleft2.pack(side=LEFT,fill=Y)
left2top=Frame(topleft2, width=410, height=100,relief="raise")
left2top.pack(side=TOP,fill=Y)
left2bottom=Frame(topleft2, width=410, height=180,relief="raise")
left2bottom.pack(side=BOTTOM,fill=X)

centerlabel=Label(left2top,text="Destination Selector ",font=("times",40,"bold"))
centerlabel.grid()
centerlabe2=Label(left2bottom,text="Destination",font=("times",30,"bold"))
centerlabe2.grid(row=1,column=0,sticky=W)
combo = ttk.Combobox(left2bottom,state='readonly',font=("times",18,"bold"),textvariable=var9)
combo['value']=['','Pathankot','Chandigarh','Amritsar','Patiala','Chennai','Delhi','Ludhiana']
combo.grid(row=1,column=1,sticky=W)
centercheck1=Checkbutton(left2bottom,text="Adult",font=("times",30),onvalue=1,offvalue=0,variable=var4)
centercheck1.grid(row=2,column=0,sticky=W)
centercheck2=Checkbutton(left2bottom,text="Child",font=("times",30),onvalue=1,offvalue=0,variable=var5)
centercheck2.grid(row=3,column=0,sticky=W)

##--------------Third Box Coding--------##
topleft3=Frame(f1a, width=375, height=300,bd=8,relief="raise")
topleft3.pack(side=LEFT,fill=Y)
thirdtop=Frame(topleft3, width=375, height=80,relief="raise")
thirdtop.pack(side=TOP,fill=Y)
thirdbottom=Frame(topleft3, width=375, height=200,relief="raise")
thirdbottom.pack(side=BOTTOM,fill=X)

thirdlabel=Label(thirdtop,text="Ticket Type ",font=("times",40,"bold"))
thirdlabel.grid()
thirdcheck1=Checkbutton(thirdbottom,text="Single",font=("times",30),onvalue=1,offvalue=0,variable=var10)
thirdcheck1.grid(row=2,column=0,sticky=W)
thirdcheck2=Checkbutton(thirdbottom,text="Return",font=("times",30),onvalue=1,offvalue=0,variable=var11)
thirdcheck2.grid(row=3,column=0,sticky=W)
thirdlabe2=Label(thirdbottom,text="No. of\n passengers ",font=("times",24,"bold"))
thirdlabe2.grid(row=4,column=0,sticky=W)
input3=Entry(thirdbottom,font=("times",12,"bold"),textvariable=var12)
input3.grid(row=4,column=1,sticky=W)

##----------Left Bottom Frame coding----------##
f2a=Frame(f1, width=970, height=400,bd=8,relief="raise")
f2a.pack(side=BOTTOM,fill=X)

##---------------Bottom first frame-------##
bottomleft1=Frame(f2a, width=1000, height=400,bd=8,relief="raise")
bottomleft1.pack(side=LEFT,fill=Y)

bottomlabel1=Label(bottomleft1,text="State Tax",font=("times",40,"bold"))
bottomlabel1.grid(row=0,column=0)
bottominput1=Label(bottomleft1,bd=8,font=("times",25,"bold"),relief="sunken",width=17,textvariable=Tax)
bottominput1.grid(row=0,column=1,sticky=W)
fill1=Label(bottomleft1,text="",font=("times",20,"bold"))
fill1.grid(row=1,column=0)
bottomlabel2=Label(bottomleft1,text="Sub Total",font=("times",40,"bold"))
bottomlabel2.grid(row=2,column=0)
bottominput2=Label(bottomleft1,bd=8,font=("times",25,"bold"),relief="sunken",width=17,textvariable=SubTotal)
bottominput2.grid(row=2,column=1,sticky=W)
fill1=Label(bottomleft1,text="",font=("times",20,"bold"))
fill1.grid(row=3,column=0)
bottomlabel3=Label(bottomleft1,text="Total Cost",font=("times",40,"bold"))
bottomlabel3.grid(row=4,column=0)
bottominput3=Label(bottomleft1,bd=8,font=("times",25,"bold"),relief="sunken",width=17,textvariable=Fee_Price)
bottominput3.grid(row=4,column=1,sticky=W)

##-------------------Bottom Second Frame----------##
bottomleft2=Frame(f2a, width=300, height=400,bd=8,relief="raise")
bottomleft2.pack(side=RIGHT)
bottomright1=Frame(bottomleft2, width=200, height=70,bd=8,relief="raise")
bottomright1.pack(side=TOP,fil=X)
bottomright2=Frame(bottomleft2, width=200, height=70,relief="raise")
bottomright2.pack(side=TOP)
bottomright3=Frame(bottomleft2, width=200, height=70,relief="raise")
bottomright3.pack(side=TOP)
bottomright4=Frame(bottomleft2, width=200, height=70,relief="raise")
bottomright4.pack(side=TOP)
bottomright5=Frame(bottomleft2, width=200, height=70,relief="raise")
bottomright5.pack(side=TOP)

inp=Entry(bottomright1,font=("times",30,"bold"),textvariable=text_input)
inp.pack(side=TOP,fill=X)
b1=Button(bottomright2,text='  7  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(7))
b1.pack(side=LEFT,fill=X)
b2=Button(bottomright2,text='  8  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(8))
b2.pack(side=LEFT,fill=X)
b3=Button(bottomright2,text='  9  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(9))
b3.pack(side=LEFT,fill=X)
badd=Button(bottomright2,text='  +  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click("+"))
badd.pack(side=LEFT,fill=X)

b4=Button(bottomright3,text='  4  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(4))
b4.pack(side=LEFT)
b5=Button(bottomright3,text='  5  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(5))
b5.pack(side=LEFT)
b6=Button(bottomright3,text='  6  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(6))
b6.pack(side=LEFT)
bsub=Button(bottomright3,text='  -   ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click("-"))
bsub.pack(side=LEFT)

b7=Button(bottomright4,text='  1  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(1))
b7.pack(side=LEFT)
b8=Button(bottomright4,text='  2  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(2))
b8.pack(side=LEFT)
b9=Button(bottomright4,text='  3  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(3))
b9.pack(side=LEFT)
bmul=Button(bottomright4,text='  *  ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click("*"))
bmul.pack(side=LEFT)

bf=Button(bottomright5,text='  0 ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click(0))
bf.pack(side=LEFT)
bz=Button(bottomright5,text='  C ',bd=8,font=("times",20,"bold"),width=5,command=Clear)
bz.pack(side=LEFT)
be=Button(bottomright5,text='  =  ',bd=8,font=("times",20,"bold"),width=5,command=equal)
be.pack(side=LEFT)
bdiv=Button(bottomright5,text='  /   ',bd=8,font=("times",20,"bold"),width=5,command=lambda:Click("/"))
bdiv.pack(side=LEFT)

##------------------------Right frame f2 coding---------------##
ft2=Frame(f2, width=520, height=120,bd=8,relief="raise")
ft2.pack(side=TOP,fill=X)

#----Right top frame coding-------#
lefttop=Label(ft2,text="Travelling Ticketing \n System",font=("times",30,"bold"))
lefttop.pack()

#------Right bottom frame coding-----#
fb2=Frame(f2, width=520, height=550,bd=8,relief="raise")
fb2.pack(side=TOP)

b1=Button(fb2,text='Class',bd=8,font=("times",20,"bold"),width=5)
b1.grid(row=0,column=0)
b2=Button(fb2,text='Ticket',bd=8,font=("times",20,"bold"),width=5)
b2.grid(row=0,column=1)
b3=Button(fb2,text='Adult',bd=8,font=("times",20,"bold"),width=5)
b3.grid(row=0,column=2)
b4=Button(fb2,text='Child',bd=8,font=("times",20,"bold"),width=5)
b4.grid(row=0,column=3)

b5=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=TicketClass)
b5.grid(row=1,column=0)
b6=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=SubTotal)
b6.grid(row=1,column=1)
b7=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=Adult_Ticket)
b7.grid(row=1,column=2)
b8=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=Child_Ticket)
b8.grid(row=1,column=3)

bb9=Button(fb2,text="From",width=5,bd=8,font=("times",20,"bold"))
bb9.grid(row=2,column=1)
bb10=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=From_Destination)
bb10.grid(row=2,column=2)
bb9=Button(fb2,text="To",width=5,bd=8,font=("times",20,"bold"))
bb9.grid(row=3,column=1)
bb10=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=To_Destination)
bb10.grid(row=3,column=2)
bb9=Button(fb2,text="Price",width=5,bd=8,font=("times",20,"bold"))
bb9.grid(row=4,column=1)
bb10=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=Fee_Price)
bb10.grid(row=4,column=2)

bb1=Button(fb2,text='Ref No.',bd=8,font=("times",20,"bold"),width=5)
bb1.grid(row=5,column=0)
bb2=Button(fb2,text='Time',bd=8,font=("times",20,"bold"),width=5)
bb2.grid(row=5,column=1)
bb3=Button(fb2,text='Date',bd=8,font=("times",20,"bold"),width=5)
bb3.grid(row=5,column=2)
bb4=Button(fb2,text='Route',bd=8,font=("times",20,"bold"),width=5)
bb4.grid(row=5,column=3)

bb5=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=Receipt_Ref)
bb5.grid(row=6,column=0)
bb6=Label(fb2,bd=8,width=11,height=3,font=("times",10,"bold"),relief='sunken',textvariable=time1)
bb6.grid(row=6,column=1)
bb7=Label(fb2,bd=8,width=11,height=3,font=("times",10,"bold"),relief='sunken',textvariable=date1)
bb7.grid(row=6,column=2)
bb8=Label(fb2,bd=8,width=11,height=3,relief='sunken',textvariable=Route)
bb8.grid(row=6,column=3)

b11=Button(fb2,text='Total',bd=8,font=("times",20,"bold"),width=5,command=Travel_Cost)
b11.grid(row=7,column=0)
b22=Button(fb2,text='Clear',bd=8,font=("times",20,"bold"),width=5,command=reset)
b22.grid(row=7,column=1)
b33=Button(fb2,text='Reset',bd=8,font=("times",20,"bold"),width=5,command=reset)
b33.grid(row=7,column=2)
b44=Button(fb2,text='Exit',bd=8,font=("times",20,"bold"),width=5,command=Exitt)
b44.grid(row=7,column=3)

f1.configure(background="black")
f2.configure(background="black")

root.mainloop()