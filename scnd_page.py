from tkinter import *
import tkinter.ttk as ttk

root=Tk()
root.geometry("1280x700")
root.title("Bus Ticketing System")

top=Frame(root, width=1280, height=100)
top.pack(side=TOP, fill=X)
f1=Frame(root, width=300, height=700)
f1.pack(side=LEFT, fill=Y)
f2=Frame(root, width=1250, height=700)
f2.pack(side=LEFT, fill=Y)

label1=Label(f2,text="Seats ",font=("times",32,"bold"),height=2)
label1.grid(row=1,column=1,sticky=W)
combo = ttk.Combobox(f2,state='readonly',font=("times",18,"bold"))
combo['value']=['','Window','Aisle']
combo.grid(row=1,column=2,sticky=W)

label2=Label(f2,text="Gender ",font=("times",32,"bold"),height=1)
label2.grid(row=2,column=1,sticky=W)
radio1=Checkbutton(f2,text="Male",font=("times",30))
radio1.grid(row=2,column=2,sticky=W)
radio2=Checkbutton(f2,text="Female",font=("times",30))
radio2.grid(row=2,column=3,sticky=W)

label3=Label(f2,text="Fare ",font=("times",32,"bold"),height=2)
label3.grid(row=3,column=1,sticky=W)
label3=Label(f2,width=14,height=3,relief='raise',bd=4)
label3.grid(row=3,column=2,sticky=W)

label4=Label(f2,text="No. of Seats ",font=("times",32,"bold"),height=1)
label4.grid(row=4,column=1,sticky=W)
combo = ttk.Combobox(f2,state='readonly',font=("times",18,"bold"))
combo['value']=['','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
combo.grid(row=4,column=2,sticky=W)

bb=Button(f2,text="Booking ",font=("times",30,"bold"),bd=4)
bb.grid(row=5,column=3,sticky=E)



root.mainloop()
