import pymysql
from tkinter import *
from tkinter import messagebox
import time;

def clear():
    vehicletype.set('')
    vehiclenumber.set('')
    charges.set('')
    status.set(' ')
    e1.configure(state='normal')

def search():
    try:
        con=pymysql.connect(user='root',password='',\
                           host='localhost',database='test')
        cur=con.cursor()
        sql="select * from parking1 where vehiclenumber='%s'"\
            %(vehiclenumber.get())
        cur.execute(sql)
        result=cur.fetchone()
        vehicletype.set(result[1])
        charges.set(result[2])
        status.set(result[3])
        con.close()
    except:
        messagebox.showinfo('no data','no such vehicle available..')
        clear()

def displayall():
    try:
        con=pymysql.connect(user='root',password='',\
                           host='localhost',db='test')
        cur=con.cursor()
        sql='select * from parking1'
        cur.execute(sql)
        result=cur.fetchall()
        f=open('details.txt','w')
        for data in result:
            f.write(str(data)+'\n')


        con.close()

        import subprocess as sp
        pName='notepad.exe'
        fName='details.txt'
        sp.Popen([pName,fName])
    except:
        messagebox.showinfo('No Data','No such data availabe...')
    finally:
        clear()

def update():
    from park import w1
    w1.destroy()
def add():
    try:
        con=pymysql.connect(user='root',password='',
                           host='localhost',db='test')
        cur=con.cursor()
        sql="insert into parking1 values('%s','%s','%s','%s')"\
             %(vehiclenumber.get(), vehicletype.get(),charges.get(),status.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('success','record added..')
    except:
        messagebox.showinfo('error','error occured..')
    finally:
        clear()


def delete():
    try:
        con=pymysql.connect(user='root',password='',\
                           host='localhost',db='test')
        cur=con.cursor()
        sql="delete from parking1 where vehiclenumber='%s'"\
             %(vehiclenumber.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('success','record deleted..')
    except:
        messagebox.showinfo('error','error occured..')
    finally:
        clear()


w1=Tk()
w1.title('parking management system')
w1.geometry('500x300')


charges=StringVar()
vehicletype = StringVar()
vehiclenumber = StringVar()
status = StringVar()

# ----------------------------------------TIME--------------------------------------------
localtime = time.asctime(time.localtime(time.time()))
# ----------------------------------------Info--------------------------------------------
lblInfo = Label(w1, font=('arial', 10, 'bold'), text="PARKING MANAGEMENT SYSTEM", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=1)
lblDateTime = Label(w1, font=('arial', 10, 'bold'), text=localtime, fg="steel Blue", bd=10, anchor='w')
lblDateTime.grid(row=1, column=1)


l1=Label(w1, text='vehiclenumber')
e1=Entry(w1, textvariable=vehiclenumber)
l2=Label(w1, text='vehicletype')
e2=Entry(w1, textvariable=vehicletype)
l3=Label(w1, text='charges')
e3=Entry(w1, textvariable=charges)
l4=Label(w1, text='status')
e4=Entry(w1, textvariable=status)



b1=Button(w1, text='search ', command=search)
b2=Button(w1, text='Add ', command=add)
b3=Button(w1, text='update ', command=update)
b4=Button(w1, text='Delete ', command=delete)
b5=Button(w1, text='clear ', command=clear)
b6=Button(w1, text='DisplayAll', command=displayall)


l1.grid(row=3, column=0)
e1.grid(row=3, column=1)
b1.grid(row=3, column=2)


l2.grid(row=4, column=0)
e2.grid(row=4, column=1)
l3.grid(row=5, column=0)
e3.grid(row=5, column=1)
l4.grid(row=6, column=0)
e4.grid(row=6, column=1)
b2.grid(row=7, column=0)
b3.grid(row=7, column=1)
b4.grid(row=8, column=0)
b5.grid(row=8, column=1)
b6.grid(row=9, column=0)


w1.mainloop()
















        
