from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

root = Tk()
root.geometry("1280x700")
root.title("Book Your Bus")
root.configure(background='black')

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=StringVar()
var11=StringVar()
var12=StringVar()
var13=StringVar()
var14=StringVar()
var15=StringVar()
var16=StringVar()

var21 = StringVar()
var22 = StringVar()
var23 = StringVar()

def cost():
    conn = sqlite3.connect('bus_detail.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bus_info WHERE Start=(?) AND Destination=(?) AND Type=(?) AND date=(?)",
              (var1.get(), var2.get(), var6.get(),var3.get()))
    conn.commit()
    rows=c.fetchone()
    var23.set(rows[4])


def search():
    conn = sqlite3.connect('bus_detail.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bus_info WHERE Start=(?) AND Destination=(?) AND Type=(?) AND date=(?)",
              (var1.get(),var2.get(),var6.get(),var3.get()))
    conn.commit()
    rows=c.fetchone()
    var7.set(rows[0])
    var8.set(rows[1])
    var9.set(rows[2])
    var10.set(rows[3])
    var11.set(rows[5])

def third():
    root = Tk()
    root.geometry("1280x700")
    root.title("Bus Ticketing System")
    root.configure(background="black")

    var31 = StringVar()
    var32 = StringVar()
    var33 = StringVar()
    var34 = StringVar()
    var35 = StringVar()
    var36 = StringVar()
    var37 = StringVar()
    var38 = StringVar()
    var39 = StringVar()
    var310 = StringVar()
    var311 = StringVar()

    def Exitt():
        qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
        if qExit > 0:
            root.destroy()
            return

    def create():
        conn = sqlite3.connect('persons1.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS `personal_info` (`Name` text, `Email` text, `Mobile` integer)')
        conn.commit()
        conn.close()

    #create()

    def connect():
        conn = sqlite3.connect('persons1.db')
        c = conn.cursor()
        c.execute('INSERT INTO `personal_info` (Name,Email,Mobile) VALUES (?, ?, ?)', (var31.get(), var32.get(), var33.get()))
        var31.set("")
        var32.set("")
        var33.set("")
        conn.commit()
        conn.close()

    left = Frame(root, width=777, height=650, bd=5, relief="raise")
    left.pack(side=LEFT, fill=Y)
    right = Frame(root, width=500, height=650, bd=5, relief="raise")
    right.pack(side=RIGHT, fill=Y)

    top = Frame(left, width=600, height=200)
    top.pack(side=TOP, fill=Y)
    toplabel = Label(top, text="Passenger Information", font=("times", 32, "bold"), height=2)
    toplabel.pack()

    f1 = Frame(left, width=600, height=500, bd=4)
    f1.pack(side=TOP, fill=Y)
    label1 = Label(f1, text="Name ", font=("times", 32, "bold"), height=2)
    label1.grid(row=1, column=1, sticky=W)
    label1 = Label(f1, text="Email ", font=("times", 32, "bold"), height=2)
    label1.grid(row=2, column=1, sticky=W)
    label1 = Label(f1, text="Mobile No. ", font=("times", 32, "bold"), height=2)
    label1.grid(row=3, column=1, sticky=W)

    entry1 = Entry(f1, font=("times", 30, "bold"), bd=4, textvariable=var31)
    entry1.grid(row=1, column=2, sticky=W)
    entry2 = Entry(f1, font=("times", 30, "bold"), bd=4, textvariable=var32)
    entry2.grid(row=2, column=2, sticky=W)
    entry3 = Entry(f1, font=("times", 30, "bold"), bd=4, textvariable=var33)
    entry3.grid(row=3, column=2, sticky=W)

    bb = Button(f1, text="Done ", font=("times", 30, "bold"), bd=4, command=connect)
    bb.grid(row=4, column=2, sticky=E)
    bb = Button(f1, text="Exit ", font=("times", 30, "bold"), bd=4, command=Exitt)
    bb.grid(row=4, column=3, sticky=E)

    topright = Frame(right, width=500, height=345, bd=5, relief="raise")
    topright.pack(side=TOP, fill=Y)
    bottomright = Frame(right, width=500, height=340, bd=5, relief="raise")
    bottomright.pack(side=BOTTOM, fill=Y)

    topright1 = Frame(topright, width=500, height=50)
    topright1.pack(side=TOP, fill=Y)
    labelr1 = Label(topright1, text="Journey Details ", font=("times", 30, "bold"))
    labelr1.pack(fill=X)

    topright2 = Frame(topright, width=500, height=290)
    topright2.pack(side=TOP, fill=Y)
    labelr1 = Label(topright2, text="Journey: ", font=("times", 20, "bold"), height=2)
    labelr1.grid(row=1, column=1, sticky=W)
    labelr2 = Label(topright2, text="Depart Time: ", font=("times", 20, "bold"), height=2)
    labelr2.grid(row=2, column=1, sticky=W)
    labelr3 = Label(topright2, text="Depart Date: ", font=("times", 20, "bold"), height=2)
    labelr3.grid(row=3, column=1, sticky=W)

    labelr4 = Label(topright2, width=18, height=2, relief='sunken', bd=4, textvariable=var34)
    labelr4.grid(row=1, column=2, sticky=W, columnspan=2)
    labelr8 = Label(topright2, text=" to ", font=("times", 20, "bold"))
    labelr8.grid(row=1, column=3, sticky=W)
    labelr5 = Label(topright2, width=18, height=2, relief='sunken', bd=4, textvariable=var35)
    labelr5.grid(row=1, column=4, sticky=W, columnspan=2)
    labelr6 = Label(topright2, width=18, height=2, relief='sunken', bd=4, textvariable=var36)
    labelr6.grid(row=2, column=2, sticky=W)
    labelr7 = Label(topright2, width=18, height=2, relief='sunken', bd=4, textvariable=var37)
    labelr7.grid(row=3, column=2, sticky=W)
    labelrs = Label(topright2, text="Seats: ", font=("times", 20, "bold"), height=2)
    labelrs.grid(row=4, column=1, sticky=W)
    labelrss = Label(topright2, width=18, height=2, relief='sunken', bd=4, textvariable=var38)
    labelrss.grid(row=4, column=2, sticky=W)
    labelrp = Label(topright2, text="Type : ", font=("times", 20, "bold"), height=1)
    labelrp.grid(row=5, column=1, sticky=W)
    labelrpp = Label(topright2, width=18, height=2, relief='sunken', bd=4, textvariable=var39)
    labelrpp.grid(row=5, column=2, sticky=W)

    bottomright1 = Frame(bottomright, width=500, height=50)
    bottomright1.pack(side=TOP, fill=Y)
    labelb1 = Label(bottomright1, text="Price Details ", font=("times", 30, "bold"), height=2)
    labelb1.pack(fill=Y)

    bottomright3 = Frame(bottomright, width=500, height=250)
    bottomright3.pack(side=TOP, fill=Y)
    labelb1 = Label(bottomright3, text="Journey Fare:- ", font=("times", 28, "bold"), width=12, height=1)
    labelb1.grid(row=1, column=1, sticky=W)
    labelb2 = Label(bottomright3, text="Base Fare: ", font=("times", 24, "bold"), height=2)
    labelb2.grid(row=2, column=1, sticky=W)
    labelb3 = Label(bottomright3, text="Total Base Fare: ", font=("times", 24, "bold"), height=2)
    labelb3.grid(row=3, column=1, sticky=W)
    labelb4 = Label(bottomright3, width=25, relief='sunken', bd=4, font=("times", 18), textvariable=var310)
    labelb4.grid(row=2, column=2, sticky=W)
    labelb5 = Label(bottomright3, width=25, relief='sunken', bd=4, font=("times", 18), textvariable=var311)
    labelb5.grid(row=3, column=2, sticky=W)

    root.mainloop()

def scnd():
    root = Tk()
    root.geometry("1280x700")
    root.title("Bus Ticketing System")

    top = Frame(root, width=1280, height=100)
    top.pack(side=TOP, fill=X)
    f1 = Frame(root, width=300, height=700)
    f1.pack(side=LEFT, fill=Y)
    f2 = Frame(root, width=1250, height=700)
    f2.pack(side=LEFT, fill=Y)

    label4 = Label(f2, text="No. of Seats ", font=("times", 32, "bold"), height=1)
    label4.grid(row=3, column=1, sticky=W)
    combo = ttk.Combobox(f2, state='readonly', font=("times", 18, "bold"), textvariable=var21)
    combo['value'] = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                      '18']
    combo.grid(row=3, column=2, sticky=W)
    btotal = Button(f2, text="Total Cost", font=("times",20, "bold"), bd=2, textvariable=var22,command=cost)
    btotal.grid(row=4, column=2, sticky=E)

    label3 = Label(f2, text="   Fare ", font=("times", 32, "bold"), height=2)
    label3.grid(row=5, column=1, sticky=W)
    label3 = Label(f2, width=14, height=3, relief='raise', bd=4, textvariable=var23)
    label3.grid(row=5, column=2, sticky=W)

    bb = Button(f2, text="Booking ", font=("times", 30, "bold"), bd=4,command=third)
    bb.grid(row=6, column=3, sticky=E)

    root.mainloop()

#####--------------------First page----------------##
#Top frame
Top =Frame(root,width=1280,height=100,bd=8,relief='raise')
a=Label(Top,text="Book Your Bus ",font=("times",36,"bold"))
a.pack()
Top.pack(side=TOP,fill=X)

#Left Bottom frame
Left_Frame=Frame(root,height=600,width=450,bd=8,relief='raise')
Left_Frame.pack(side=LEFT,fill=Y)
Left_Frame3=Frame(Left_Frame,height=300,width=450,bd=8)
Left_Frame3.pack(side=TOP,fill=X)
Left_Frame1=Frame(Left_Frame,height=300,width=450,bd=8)
Left_Frame1.pack(side=TOP,fill=X)
Left_Frame2=Frame(Left_Frame,height=300,width=450,bd=8)
Left_Frame2.pack(side=TOP,fill=X)
Left_Frame4=Frame(Left_Frame,height=300,width=450,bd=8)
Left_Frame4.pack(side=TOP,fill=X)


b=Label(Left_Frame3,text="Search Your Bus",width=14,font=("time",30,"bold"),justify="center")
b.pack()

c=Label(Left_Frame1,text="From:",width=12,font=("time",30,"bold"))
c.grid(row=0,column=0,sticky=W)
combo1=ttk.Combobox(Left_Frame1,width=30,state='readonly',textvariable=var1)
combo1['value']=['','Delhi','Ludhiana','Jalandhar','Amritsar','Chandigarh']
combo1.grid(row=0,column=1,sticky=W)

d=Label(Left_Frame1,text="To:",width=12,font=("time",30,"bold"))
d.grid(row=1,column=0,sticky=W)
combo2=ttk.Combobox(Left_Frame1,width=30,state='readonly',textvariable=var2)
combo2['value']=['','Chandigarh','Delhi','Ludhiana','Jalandhar','Amritsar']
combo2.grid(row=1,column=1,sticky=W)

e=Label(Left_Frame2,text="Date:",width=12,font=("time",30,"bold"))
e.grid(row=0,column=0,sticky=W)
combo3=ttk.Combobox(Left_Frame2,width=8,state='readonly',textvariable=var3)
combo3['value']=['','1','2','3','4','5','6','7','8','9','10','11','12','13','14',
                '15','16','17','18','19','20','21','22','23','24','25','26','27',
                '28','29','30','31']
combo3.grid(row=0,column=1,sticky=W)

combo4=ttk.Combobox(Left_Frame2,width=8,state='readonly',textvariable=var4)
combo4['value']=['','1','2','3','4','5','6','7','8','9','10','11','12']
combo4.grid(row=0,column=2,sticky=W)

combo5=ttk.Combobox(Left_Frame2,width=8,state='readonly',textvariable=var5)
combo5['value']=['','2018','2019','2020','2021','2022','2023','2025']
combo5.grid(row=0,column=3,sticky=W)

labelss=Label(Left_Frame4,text="Type ",font=("time",30,"bold"),width=12)
labelss.grid(row=1,column=1,sticky=W)
combo = ttk.Combobox(Left_Frame4,state='readonly',width=30,textvariable=var6)
combo['value']=['','AC','Non-AC']
combo.grid(row=1,column=2,sticky=W)

btnSearch=Button(Left_Frame4,text="Search",width=7,bd=6,fg="black",
                 font=("times",15,"bold"),command=search)
btnSearch.grid(row=2,column=2,sticky=E)


#Right Bottom frame
Right_Frame=Frame(root,height=600,width=780,bd=8,relief='raise')
Right_Frame.pack(side=LEFT,fill=Y)
Right_Frame1=Frame(Right_Frame)
Right_Frame1.pack(side=TOP,fill=Y)
Right_Frame2=Frame(Right_Frame)
Right_Frame2.pack(side=TOP,fill=Y)

aa=Label(Right_Frame1,text="Bus Avaliability",width=44,font=("time",28,"bold"))
aa.pack()

lb1a=Label(Right_Frame2,font=("times",14,"bold"),text="Bus Name",bd=10,width=11,relief="raise")
lb1a.grid(row=0,column=0)

lb2a=Label(Right_Frame2,font=("times",14,"bold"),text="Type",bd=10,width=11,relief="raise")
lb2a.grid(row=0,column=1)

lb3a=Label(Right_Frame2,font=("times",14,"bold"),text="Depart",bd=10,width=11,relief="raise")
lb3a.grid(row=0,column=2)

lb4a=Label(Right_Frame2,font=("times",14,"bold"),text="Arive",bd=10,width=11,relief="raise")
lb4a.grid(row=0,column=3)

lb5a=Label(Right_Frame2,font=("times",14,"bold"),text="Available",bd=10,width=11,relief="raise")
lb5a.grid(row=0,column=4)

btnslct1=Button(Right_Frame2,text="Select",width=7,bd=6,fg="black",
                 font=("times",15,"bold"))
btnslct1.grid(row=2,column=0,sticky=W)
btnselct2=Button(Right_Frame2,text="Select",width=7,bd=6,fg="black",
                 font=("times",15,"bold"))
btnselct2.grid(row=4,column=0,sticky=W)


lbA=Label(Right_Frame2,font=("times",14,"bold"),height=5,width=12,relief="sunken",textvariable=var7)
lbA.grid(row=1,column=0)
lbA1=Label(Right_Frame2,font=("times",14,"bold"),height=5,width=12,relief="sunken",textvariable=var8)
lbA1.grid(row=1,column=1)
lbA2=Label(Right_Frame2,font=("times",14,"bold"),height=5,width=12,relief="sunken",textvariable=var9)
lbA2.grid(row=1,column=2)
lbA3=Label(Right_Frame2,font=("times",14,"bold"),height=5,width=12,relief="sunken",textvariable=var10)
lbA3.grid(row=1,column=3)
lbA4=Label(Right_Frame2,font=("times",14,"bold"),height=5,width=12,relief="sunken",textvariable=var11)
lbA4.grid(row=1,column=4)
lbB=Label(Right_Frame2,font=("times",14,"bold"),width=12,height=5,relief="sunken",textvariable=var12)
lbB.grid(row=3,column=0)
lbB1=Label(Right_Frame2,font=("times",14,"bold"),width=12,height=5,relief="sunken",textvariable=var13)
lbB1.grid(row=3,column=1)
lbB2=Label(Right_Frame2,font=("times",14,"bold"),width=12,height=5,relief="sunken",textvariable=var14)
lbB2.grid(row=3,column=2)
lbB3=Label(Right_Frame2,font=("times",14,"bold"),width=12,height=5,relief="sunken",textvariable=var15)
lbB3.grid(row=3,column=3)
lbB4=Label(Right_Frame2,font=("times",14,"bold"),width=12,height=5,relief="sunken",textvariable=var16)
lbB4.grid(row=3,column=4)


btnnext=Button(Right_Frame2,text="Next >>",width=7,bd=6,fg="black",
                 font=("times",15,"bold"),command=scnd)
btnnext.grid(row=5,column=4)


root.mainloop()