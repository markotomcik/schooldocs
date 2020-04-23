import tkinter

def uloz():
    with open("kroky.txt", "a") as subor:
        subor.write(krok.get() + '\n')
    nacitaj()

def nacitaj():
    with open("kroky.txt", "r") as subor:
        obsah=subor.read().split()
        kroky=[]
        for riadok in obsah:
            kroky.append(int(riadok))
        spolu.set(sum(kroky))

def reset():
    open("kroky.txt", "w").close()
    krok.set(0)
    spolu.set(0)

okno=tkinter.Tk()
okno.title("Výdavky")

tkinter.Label(okno, text="Počet krokov dnes prejdených:", width=50).grid(row=0,column=0)
krok=tkinter.StringVar()
tkinter.Entry(okno, textvariable=krok).grid(row=0,column=10)
krok.set(0)

tkinter.Label(okno, text="Celkovo prejdených krokov:", width=50).grid(row=10,column=0)
spolu=tkinter.StringVar()
tkinter.Entry(okno, textvariable=spolu).grid(row=10,column=10)
nacitaj()

tkinter.Button(okno, width=30, text="ulož", command=uloz).grid(row=20,column=10)
tkinter.Button(okno, width=30, text="reset", command=reset).grid(row=30,column=10)

okno.mainloop()