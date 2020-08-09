from tkinter import*
from tkinter import ttk

def Submitt():
        print(combo.get())

w1=Tk()
texto=StringVar()
#texto.set('hi')
combo=ttk.Combobox(w1)
combo.place(x=50,y=100)
combo['value']=('car','bike','truck','jcb')
boton=Button(w1,command=Submitt,text="Submitt").place(x=80,y=150)
w1.geometry("300x300")
