import tkinter 

def nacitaj():
    with open('jazdy.txt', 'r') as subor:
        obsah=subor.read().split()
        jazdy=[]
        for jazda in obsah:
            jazdy.append(float(jazda))
    pocet.set(len(jazdy))
    priemer.set(sum(jazdy)/len(jazdy))
    celkom.set(sum(jazdy))
    zarobok.set(sum(jazdy) * 1.4)

okno=tkinter.Tk()
okno.title("Evidencia jázd")
tkinter.Label(okno, text="Počet jázd:", width=30).grid(row=0,column=0)
pocet=tkinter.StringVar()
tkinter.Entry(okno, textvariable=pocet).grid(row=0,column=1)
tkinter.Label(okno, text="Priemerná vzdielenosť (v km):", width=30).grid(row=1,column=0)
priemer=tkinter.StringVar()
tkinter.Entry(okno, textvariable=priemer).grid(row=1,column=1)
tkinter.Label(okno, text="Celková vzdielenosť (v km):", width=30).grid(row=2,column=0)
celkom=tkinter.StringVar()
tkinter.Entry(okno, textvariable=celkom).grid(row=2,column=1)
tkinter.Label(okno, text="Zarobená suma (v €):", width=30).grid(row=3,column=0)
zarobok=tkinter.StringVar()
tkinter.Entry(okno, textvariable=zarobok).grid(row=3,column=1)
tkinter.Button(okno,width=30, text="Načítaj hodnoty", command=nacitaj).grid(row=4,column=1)
okno.mainloop()
