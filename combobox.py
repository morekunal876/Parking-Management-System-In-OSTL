from tkinter import *
#from tkinter.ttk import Combobox
from tkinter import ttk
import time;
import  pymysql
from tkinter import messagebox


w1=Tk()

charges=StringVar()
vehicletype=StringVar()
vehiclenumber = StringVar()
extracharges = StringVar()
texto=StringVar()


# ----------------------------------------TIME--------------------------------------------
localtime = time.asctime(time.localtime(time.time()))
# ----------------------------------------Info--------------------------------------------
lblInfo = Label(w1, font=('arial', 10, 'bold'), text="PARKING MANAGEMENT SYSTEM", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=1)
lblDateTime = Label(w1, font=('arial', 10, 'bold'), text=localtime, fg="steel Blue", bd=10, anchor='w')
lblDateTime.grid(row=1, column=1)

def clear():
    vehicletype.set('')
    charges.set(' ')

def Submitt():
    try:
        #print(vehicletype.get())
        con = pymysql.connect(user='root', password='', \
                              host='localhost', database='test')
        cur = con.cursor()
        sql = "SELECT * FROM parking rate WHERE vehicletype='%s'" \
              % (vehicletype.get())
        print(vehicletype.get())
        cur.execute(sql)
        result = cur.fetchone()
        vehicletype.set(result[1])
        charges.set(result[2])
        con.close()
    except:
        messagebox.showinfo('no data', 'no such vehicle available..')
        clear()


def update():
    try:

        print(vehicletype.get())
        con=pymysql.connect(user='root',password='',\
                           host='localhost',db='test')
        cur=con.cursor()
        sql="update parking rate set charges='%s' where vehicletype='%s'"\
            %(charges.get(),vehicletype.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('success','record updated..')
    except:
        messagebox.showinfo('error','error occured..')
        clear()

v=["car", "bike", "truck","jcb"]

vehicletype=ttk.Combobox(w1, values=v)
#combo.pack()
vehicletype.place(x=90,y=80)



w1.geometry("300x300+120+100")
l1=Label(w1, text='vehicletype')
l1.place(x=30,y=80)

l2=Label(w1, text='charges')
e2=Entry(w1, textvariable=charges)
l2.place(x=30,y=150)
e2.place(x=90,y=150)
b1=Button(w1, text='update ', command=update)
b1.place(x=80,y=200)
b2=Button(w1,command=Submitt,text="Submitt").place(x=100,y=110)
w1.mainloop()
