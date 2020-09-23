from tkinter import *
from tkinter.constants import *
from math import sqrt

root = Tk()
root.minsize(200, 250)
root.resizable(width=False, height=False)
root.title("Calculadora")
root.wm_iconbitmap('calculator_icon.ico')
root.configure(background='white')

e = Entry(root, width=16, borderwidth=5, font=("Calibri Light", 16), justify=RIGHT, state=NORMAL)
e.insert(0, 0)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=5)
e.get()


def button_add(x):
    codus = e.get()
    cadus = list(codus)[::-1]

    if x == ".":
        for num in cadus:
            if num == ".":
                return
        return e.insert(END, x)

    if x not in ["+", "-", "*", "/", "."]:
        if codus == "0" or codus == "0.0":
            e.delete(0)
            return e.insert(END, x)
        else:
            return e.insert(END, x)

    if x in ["+", "-", "*", "/"]:
        if codus == "0" or codus == "0.0":
            return
        if cadus[0] not in ["+", "-", "*", "/", "."]:
            return e.insert(END, x)
        else:
            return


def button_clear():
    e.delete(0, END)
    e.insert(0, 0)
    return


def button_cancel_entry():
    e.delete(0, END)
    e.insert(0, 0)
    # Depois adcionar registros.
    return


def button_return():
    codus = e.get()
    cadus = list(codus)[::-1]
    if codus != "0":
        e.delete(len(cadus)-1)
    if len(codus) == 1:
        e.delete(0)
        e.insert(0, 0)
    return


def button_module():
    codus = e.get()
    codus = int(codus)
    if codus > 0:
        e.insert(0, "-")
    if codus < 0:
        e.delete(0)
    return


def button_inverse():
    codus = e.get()
    codus = float(codus)
    codus = 1/codus
    e.delete(0, END)
    e.insert(0, codus)
    return


def button_raizq():
    codus = e.get()
    if float(codus) > 0:
        codus = sqrt(float(codus))
        e.delete(0, END)
        e.insert(0, codus)
    return


def button_eq():
    codus = e.get()
    cadus = list(codus)[::-1]
    if cadus[0] in ["*", "/", "+", "-"]:
        e.delete(0, END)
        return e.insert(0, 0)
    if cadus[0] in ["."]:
        return e.delete(len(cadus)-1)
    else:
        e.delete(0, END)
        return e.insert(0, eval(codus))


button_1 = Button(root, text="1", width=1, padx=13, pady=0, command=lambda: button_add(1), font=("Calibri Light", 14))
button_2 = Button(root, text="2", width=1, padx=13, pady=0, command=lambda: button_add(2), font=("Calibri Light", 14))
button_3 = Button(root, text="3", width=1, padx=13, pady=0, command=lambda: button_add(3), font=("Calibri Light", 14))
button_less = Button(root, text="-", width=1, padx=13, pady=0, command=lambda: button_add("-"), font=("Calibri Light", 14))

button_4 = Button(root, text="4", width=1, padx=13, pady=0, command=lambda: button_add(4), font=("Calibri Light", 14))
button_5 = Button(root, text="5", width=1, padx=13, pady=0, command=lambda: button_add(5), font=("Calibri Light", 14))
button_6 = Button(root, text="6", width=1, padx=13, pady=0, command=lambda: button_add(6), font=("Calibri Light", 14))
button_prod = Button(root, text="*", width=1, padx=13, pady=0, command=lambda: button_add("*"), font=("Calibri Light", 14))
button_frac = Button(root, text="1/x", width=1, padx=13, pady=0, command=button_inverse, font=("Calibri Light", 14))

button_7 = Button(root, text="7", width=1, padx=13, pady=0, command=lambda: button_add(7), font=("Calibri Light", 14))
button_8 = Button(root, text="8", width=1, padx=13, pady=0, command=lambda: button_add(8), font=("Calibri Light", 14))
button_9 = Button(root, text="9", width=1, padx=13, pady=0, command=lambda: button_add(9), font=("Calibri Light", 14))
button_div = Button(root, text="÷", width=1, padx=13, pady=0, command=lambda: button_add("/"), font=("Calibri Light", 14))
button_mod = Button(root, text="%", width=1, padx=13, pady=0, command=lambda: button_add, font=("Calibri Light", 14))

button_back = Button(root, text="←", width=1, padx=13, pady=0, command=button_return, font=("Calibri Light", 14))
button_ce = Button(root, text="↻", width=1, padx=13, pady=0, command=button_cancel_entry, font=("Calibri Light", 14))
button_c = Button(root, text="C", width=1, padx=13, pady=0, command=button_clear, font=("Calibri Light", 14))
button_pl = Button(root, text="±", width=1, padx=13, pady=0, command=button_module, font=("Calibri Light", 14))
button_raizq = Button(root, text="√", width=1, padx=13, pady=0, command=button_raizq, font=("Calibri Light", 14))

button_mc = Button(root, text="MC", width=1, padx=13, pady=0, command=lambda: button_add, font=("Calibri Light", 14))
button_mr = Button(root, text="MR", width=1, padx=13, pady=0, command=lambda: button_add, font=("Calibri Light", 14))
button_ms = Button(root, text='MS', width=1, padx=13, pady=0, command=lambda: button_add, font=("Calibri Light", 14))
button_mplus = Button(root, text="M+", width=1, padx=13, pady=0, command=lambda: button_add, font=("Calibri Light", 14))
button_mless = Button(root, text="M-", width=1, padx=13, pady=0, command=lambda: button_add, font=("Calibri Light", 14))

button_0 = Button(root, text="0", padx=32, pady=0, command=lambda: button_add(0), font=("Calibri Light", 14))
button_virg = Button(root, text=".", width=1, padx=13, pady=0, command=lambda: button_add("."), font=("Calibri Light", 14))
button_plus = Button(root, text="+", width=1, padx=13, pady=0, command=lambda: button_add("+"), font=("Calibri Light", 14))
button_equal = Button(root, text="=", width=1, padx=13, pady=19, command=button_eq, font=("Calibri Light", 14))

button_0.grid(row=6, column=0, columnspan=2)
button_virg.grid(row=6, column=2)
button_plus.grid(row=6, column=3)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_less.grid(row=5, column=3)
button_equal.grid(row=5, column=4, rowspan=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_prod.grid(row=4, column=3)
button_frac.grid(row=4, column=4)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_div.grid(row=3, column=3)
button_mod.grid(row=3, column=4)

button_back.grid(row=2, column=0)
button_ce.grid(row=2, column=1)
button_c.grid(row=2, column=2)
button_pl.grid(row=2, column=3)
button_raizq.grid(row=2, column=4)

button_mc.grid(row=1, column=0)
button_mr.grid(row=1, column=1)
button_ms.grid(row=1, column=2)
button_mplus.grid(row=1, column=3)
button_mless.grid(row=1, column=4)

root.mainloop()
