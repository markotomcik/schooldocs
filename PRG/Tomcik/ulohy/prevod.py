import tkinter

def ctof():
    f.set(9/5 * float(c.get()) + 32)

def ftoc():
    c.set((float(f.get()) - 32) * 5/9)

def koniec():
    okno.destroy()
    
okno=tkinter.Tk()
okno.title("Test čísla")

tkinter.Label(okno, text="°C", width=20).grid(row=0,column=0)
c = tkinter.StringVar()
tkinter.Entry(okno, textvariable=c, width=18).grid(row=10,column=0)

tkinter.Label(okno, text="°F", width=20).grid(row=0,column=10)
f = tkinter.StringVar()
tkinter.Entry(okno, textvariable=f, width=18).grid(row=10,column=10)

tkinter.Button(okno, width=20, text="°C -> °F", command=ctof).grid(row=20,column=0)
tkinter.Button(okno, width=20, text="°C <- °F", command=ftoc).grid(row=20,column=10)

tkinter.Button(okno, width=20, text="koniec", command=koniec).grid(row=30, column=10)

okno.mainloop()
