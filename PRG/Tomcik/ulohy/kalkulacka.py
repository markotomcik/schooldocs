import tkinter

def spocitaj():
    vysledok.set(int(a.get()) + int(b.get()))

def koniec():
    okno.destroy()
    
okno=tkinter.Tk()
okno.title("Test čísla")

tkinter.Label(okno, text="Zadaj číslo A:", width=20).grid(row=0,column=0)
a = tkinter.StringVar()
tkinter.Entry(okno, textvariable=a, width=18).grid(row=0,column=1)

tkinter.Label(okno, text="Zadaj číslo B:", width=20).grid(row=1,column=0)
b = tkinter.StringVar()
tkinter.Entry(okno, textvariable=b, width=18).grid(row=1,column=1)

tkinter.Label(okno, text="Výsledok:", width=20).grid(row=2,column=0)
vysledok=tkinter.StringVar()
tkinter.Entry(okno, textvariable=vysledok, width=18).grid(row=2,column=1)

tkinter.Button(okno, width=20, text="spočítaj", command=spocitaj).grid(row=3,column=1)
tkinter.Button(okno, width=20, text="zruš", command=koniec).grid(row=4,column=1)

okno.mainloop()
