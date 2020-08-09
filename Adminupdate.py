
import time;
import pymysql
from pymysql import *
from tkinter import *
from tkinter.ttk import Combobox





w1=Tk()
w1.title('parking management system')
#w1.geometry('300x300')



charges=StringVar()
vehicletype=StringVar()
vehiclenumber = StringVar()
extracharges = StringVar()

# ----------------------------------------TIME--------------------------------------------
localtime = time.asctime(time.localtime(time.time()))
# ----------------------------------------Info--------------------------------------------
lblInfo = Label(w1, font=('arial', 10, 'bold'), text="PARKING MANAGEMENT SYSTEM", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=1)
lblDateTime = Label(w1, font=('arial', 10, 'bold'), text=localtime, fg="steel Blue", bd=10, anchor='w')
lblDateTime.grid(row=1, column=1)


def update():
    from last import w1
    try:
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


v=["c++", "c", "java"]

combo=Combobox(w1, values=v)
#combo.pack()



w1.geometry("300x300+120+100")


w1.mainloop()

