import tkinter 

def odpocitaj():
    tkinter.Label(okno, text=str(cas), fg="green", font=("Helvetica", 70, "bold")).pack()

okno=tkinter.Tk()
okno.title("Evidencia jázd")

tkinter.Label(okno, text="Zadaj čas na odpočítavanie:").pack()
cas=tkinter.StringVar()
tkinter.Entry(okno, textvariable=cas).pack()

odpocitaj()

tkinter.Button(okno, text="ŠTART", command=odpocitaj).pack()

okno.mainloop()
