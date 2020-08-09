from tkinter import *
from tkinter import simpledialog
import time;
import pymysql


def Car():
    car = simpledialog.askstring("input string", "ENTER CAR NUMBER")
    print(car)

    charge = simpledialog.askinteger("input string", "ENTER THE CHARGE OF CAR")
    print(charge)

    extracharge = simpledialog.askinteger("input string", "ENTER THE EXTRACHARGE OF CAR")
    print(extracharge)

    tax = simpledialog.askfloat("input string", "ENTER THE TAXT OF CAR"
                                                "")
    print(tax)

    cost = float(charge + extracharge) * tax
    print(cost)
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="test")
    cur = conn.cursor()
    sql = "insert into parking values('%s','%s','%s','%s','%s','%s')" \
          % ('Car', car, charge, extracharge, tax, cost)
    cur.execute(sql)
    """cur.execute("INSERT INTO PARKING(vehical name,ID,charges,extracharges,Taxt,Cost) VALUES('Car',car,charge,extracharge,tax,cost);")"""
    conn.commit()
    conn.close()


def Bike():
    Bike = simpledialog.askstring("input string", "ENTER THE BIKE NUMBER")
    print(Bike)

    charge = simpledialog.askfloat("input string", "ENTER THE CHARGE OF BIKE")
    print(charge)

    extracharge = simpledialog.askfloat("input string", "ENTER THE EXTRACHARGE OF BIKE")
    print(extracharge)

    tax = simpledialog.askfloat("input string", "ENTER THE TAXT OF BIKE")
    print(tax)

    cost = float((charge + extracharge )* tax)
    print(cost)

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="test")
    cur = conn.cursor()
    sql = "insert into parking values('%s','%s','%s','%s','%s','%s')" \
          % ('Bike', Bike, charge, extracharge, tax, cost)
    cur.execute(sql)

    conn.commit()
    conn.close()


def Truck():
    Truck = simpledialog.askstring("input string", "ENTER THE TRUCK NUMBER")
    print(Truck)

    charge = simpledialog.askfloat("input string", "ENTER THE CHARGE OF TRUCK")
    print(charge)

    extracharge = simpledialog.askfloat("input string", "ENTER THE EXTRACHARGE OF TRUCK")
    print(extracharge)

    tax = simpledialog.askfloat("input string", "ENTER THE TXAT OF TRUCK")
    print(tax)

    cost = float((charge  + extracharge) * tax)
    print(cost)

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="test")
    cur = conn.cursor()
    sql = "insert into parking values('%s','%s','%s','%s','%s','%s')" \
          % ('Truck', Truck, charge, extracharge, tax, cost)
    cur.execute(sql)

    conn.commit()
    conn.close()


def Jcb():
    Jcb = simpledialog.askstring("input string", "ENTER THE JCB NUMBER")
    print(Jcb)

    charge = simpledialog.askfloat("input string", "ENTER THE CHARGE OF JCB")
    print(charge)

    extracharge = simpledialog.askfloat("input string", "ENTER THE EXTRACHARGE OF JCB")
    print(extracharge)

    tax = simpledialog.askfloat("input string", "ENTER THE TAXT OF JCB")
    print(tax)

    cost = float((charge + extracharge) * tax)
    print(cost)

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="test")
    cur = conn.cursor()
    sql = "insert into parking values('%s','%s','%s','%s','%s','%s')" \
          % ('Jcb', Jcb, charge, extracharge, tax, cost)
    cur.execute(sql)

    conn.commit()
    conn.close()


def Exit():
    root.destroy()


root = Tk()
car1 = StringVar
charge1 = StringVar
extracharge1 = StringVar
tax1 = StringVar
cost1 = StringVar
Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=1700, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# ----------------------------------------TIME--------------------------------------------
localtime = time.asctime(time.localtime(time.time()))
# ----------------------------------------Info--------------------------------------------
lblInfo = Label(Tops, font=('arial', 10, 'bold'), text="PARKING MANAGEMENT SYSTEM", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblDateTime = Label(Tops, font=('arial', 10, 'bold'), text=localtime, fg="steel Blue", bd=10, anchor='w')
lblDateTime.grid(row=1, column=0)

button = Button(f1, padx=16, pady=8, bd=12, fg="black", font=('arrial', 18, 'bold'),
                width=8, text="Car", bg="powder blue", command=Car).grid(row=0, column=1)

button = Button(f1, padx=16, pady=8, bd=12, fg="black", font=('arrial', 18, 'bold'),
                width=8, text="Bike", bg="powder blue", command=Bike).grid(row=0, column=2)

button = Button(f1, padx=16, pady=8, bd=12, fg="black", font=('arrial', 18, 'bold'),
                width=8, text="Truck", bg="powder blue", command=Truck).grid(row=0, column=3)

button = Button(f1, padx=16, pady=8, bd=12, fg="black", font=('arrial', 18, 'bold'),
                width=8, text="Jcb", bg="powder blue", command=Jcb).grid(row=0, column=4)

button = Button(f1, padx=16, pady=8, bd=12, fg="black", font=('arrial', 18, 'bold'),
                width=8, text="exit", bg="powder blue", command=Exit).grid(row=0, column=5)

root.geometry("1600x800+0+0")

root.mainloop()
