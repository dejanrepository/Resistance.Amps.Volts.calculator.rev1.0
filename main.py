from tkinter import *
import math
from PIL import ImageTk, Image

root = Tk()
root.title('Simple Wattage calculator. Made by Dejan')
root.geometry("350x495")
root.bind("<Escape>", quit)

img = ImageTk.PhotoImage(Image.open('img/wattageC.gif'))
slika = Label(image=img)
slika.grid(row=6, columnspan=4)


def equalpress():

    global current
    c = current.get()
    v = voltage.get()
    r = resistance.get()
    w = wattage.get()

    if c == '':
        c = '0'
    if v == '':
        v = '0'
    if r == '':
        r = '0'
    if w == '':
        w = '0'

    elif r == '0' and c == '0':
        r = float(w) / float(v)
        resistance.delete(0, END)
        temp = round(r,3)
        resistance.insert(0, temp)

        c = float(v) / float(temp)
        current.delete(0, END)
        temp = round(c,3)
        current.insert(0, temp)
    elif w == '0' and v == '0':
        v = float(r) * float(c)
        voltage.delete(0, END)
        temp = round(v,3)
        voltage.insert(0, temp)
        w = float(c) * float(v)
        wattage.delete(0, END)
        temp = round(w,3)
        wattage.insert(0, temp)
    elif c == '0' and w == '0':
        c = float(v) / float(r)
        current.delete(0, END)
        temp = round(c,3)
        current.insert(0, temp)
        w = float(c) * float(v)
        wattage.delete(0, END)
        temp = round(w,3)
        wattage.insert(0, temp)
    elif w == '0' and r == '0':
        w = float(c) * float(v)
        wattage.delete(0, END)
        temp = round(w, 3)
        wattage.insert(0, temp)

        r = float(v) / float(c)
        resistance.delete(0, END)
        temp = round(r, 3)
        resistance.insert(0, temp)
    elif c == '0' and v == '0':
        c = math.sqrt(float(w) / float(r))
        current.delete(0, END)
        temp = round(c, 3)
        current.insert(0, temp)
        v = math.sqrt(float(w) * float(r))
        voltage.delete(0, END)
        temp = round(v, 3)
        voltage.insert(0, temp)
    elif v == '0' and r == '0':
        v = float(w) / float(c)
        voltage.delete(0, END)
        temp = round(v, 3)
        voltage.insert(0, temp)
        r = float(w) / (float(c) * float(c))
        resistance.delete(0, END)
        temp = round(r, 3)
        resistance.insert(0, temp)


def clear():
    current.delete(0, END)
    current.insert(0, 0)
    voltage.delete(0, END)
    voltage.insert(0, 0)
    wattage.delete(0, END)
    wattage.insert(0, 0)
    resistance.delete(0, END)
    resistance.insert(0, 0)


current_label = Label(root, text="Current(A): ").grid(row=1, column=0)
current = Entry(root, width=25)
current.grid(row=1, column=1, columnspan = 6)
current.insert(0, 0)

voltage_label = Label(root, text="Voltage(V): ").grid(row=2, column=0)
voltage = Entry(root, width=25)
voltage.grid(row=2, column=1, columnspan = 6)
voltage.insert(0, 0)

resistance_label = Label(root, text="Resistance(Ohm): ").grid(row=3, column=0)
resistance = Entry(root, width=25)
resistance.grid(row=3, column=1, columnspan = 6)
resistance.insert(0, 0)

wattage_label = Label(root, text="Wattage(P): ").grid(row=4, column=0)
wattage = Entry(root, width=25)
wattage.grid(row=4, column=1, columnspan = 6)
wattage.insert(0, 0)

equalbutton = Button(root, text="Calculate", width=15, height=3, command=equalpress)
equalbutton.grid(row=5, columnspan=3, pady=10, padx=20)

clearbutton = Button(root, text="Clear", width=15, height=3, command=clear)
clearbutton.grid(row=5, columnspan=3, column=3, pady=10, padx=15)

root.mainloop()
