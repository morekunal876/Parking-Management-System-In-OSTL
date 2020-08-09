from tkinter import *
import os
import pymysql

def user_pass():
    if ((user.get()=='abhi') and (passwd.get()=='1234') or (user.get()=='kunal') and (passwd.get()=='5678') ):
        root.destroy()
        from lastpro import  w1

        
    else:
        message=Label(text='Username or Password incorrect')
        message.grid(row=6,column=2)

def admin_login():
    root.destroy()
    from Admin import w1

root=Tk()
root.geometry('425x225')
root.title("Login Window")
user=StringVar()
passwd=StringVar()

l1 = Label(root,text="Username")
e=Entry(root)
l1.grid(row=1,column=1,pady=20)
e=Entry(root,textvariable=user)
e.grid(row=1,column=2)

l2 = Label(root,text="Password")
e1=Entry(root)
l2.grid(row=2,column=1,pady=10)
e1=Entry(root,show='*',textvariable=passwd)
e1.grid(row=2,column=2)
b1=Button(root,text="LOGIN!",command=user_pass).grid(row=3,column=2)
b2=Button(root,text="ADMIN LOGIN!",command=admin_login).grid(row=3,column=3)


root.mainloop()























