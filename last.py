import pymysql
from tkinter import *
from tkinter import messagebox

def clear():
    vehicletype.set('')
    vehiclenumber.set('')
    charges.set('')
    extracharges.set(' ')
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
        extracharges.set(result[3])
        status.set(result[4])
        con.close()
    except:
        messagebox.showinfo('no data','no such vehicle available..')
        clear()



def update():
    #w1.destroy()
    try:
           con=pymysql.connect(user='root',password='',\
                              host='localhost',db='test')
           cur=con.cursor()
           sql="update parking1 set vehicletype='%s',charges='%s',extracharges='%s',status='%s' where vehiclenumber='%s'"\
                %(vehicletype.get(), charges.get(),extracharges.get(),status.get() ,vehiclenumber.get())
           cur.execute(sql)
           con.commit()
           con.close()
           messagebox.showinfo('success','record updated..')
    except:
           messagebox.showinfo('error','error occured..')
    finally:
           clear()

def add():
    try:
        con=pymysql.connect(user='root',password='',
                           host='localhost',db='test')
        cur=con.cursor()
        sql="insert into parking1 values('%s','%s','%s','%s','%s')"\
             % (vehiclenumber.get(), vehicletype.get(), charges.get(),extracharges.get(),status.get())
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
w1.geometry('600x200')


charges=StringVar()
vehicletype = StringVar()
vehiclenumber = StringVar()
extracharges = StringVar()
status = StringVar()


l1=Label(w1, text='vehiclenumber')
e1=Entry(w1, textvariable=vehiclenumber)
l2=Label(w1, text='vehicletype')
e2=Entry(w1, textvariable=vehicletype)
l3=Label(w1, text='charges')
e3=Entry(w1, textvariable=charges)
l4=Label(w1, text='extracharges')
e4=Entry(w1, textvariable=extracharges)
l5=Label(w1, text='Status')
e5=Entry(w1, textvariable=status)


b1=Button(w1, text='search ', command=search)
b2=Button(w1, text='Add ', command=add)
b3=Button(w1, text='update ', command=update)
b4=Button(w1, text='Delete ', command=delete)
b5=Button(w1, text='clear ', command=clear)

l1.grid(row=1, column=0)
e1.grid(row=1, column=1)
b1.grid(row=1, column=2)


l2.grid(row=2, column=0)
e2.grid(row=2, column=1)
l3.grid(row=3, column=0)
e3.grid(row=3, column=1)
l4.grid(row=4, column=0)
e4.grid(row=4, column=1)
l5.grid(row=5, column=0)
e5.grid(row=5, column=1)

b2.grid(row=6, column=0)
b3.grid(row=6, column=1)
b4.grid(row=7, column=0)
b5.grid(row=7, column=1)

w1.mainloop()
















        
