from tkinter import *
import os
import pymysql

def user_pass():
    if ((user.get()=='Admin') and (passwd.get()=='admin') or (user.get()=='Admin1') and (passwd.get()=='admin1') ):
        root.destroy()
        from combobox import  w1

        
    else:
        message=Label(text='Username or Password incorrect')
        message.grid(row=6,column=2)

root=Tk()
root.geometry('425x225')
root.title(" Admin Login")
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
b=Button(root,text="LOGIN!",command=user_pass).grid(row=3,column=2)

root.mainloop()























