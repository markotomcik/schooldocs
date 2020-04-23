import tkinter

def uloz():
    with open("nakupy.txt", "a") as subor:
        subor.write(tovar.get() + ' ' + cena.get() + '\n')

okno=tkinter.Tk()
okno.title("Výdavky")

tkinter.Label(okno, text="Čo sa kúpilo:", width=50).grid(row=0,column=0)
tovar=tkinter.StringVar()
tkinter.Entry(okno, textvariable=tovar).grid(row=0,column=10)

tkinter.Label(okno, text="Cena (€):", width=50).grid(row=10,column=0)
cena=tkinter.StringVar()
tkinter.Entry(okno, textvariable=cena).grid(row=10,column=10)

tkinter.Button(okno, width=30, text="ulož", command=uloz).grid(row=20,column=10)

okno.mainloop()