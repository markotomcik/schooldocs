import tkinter

def rozsviet(objekt, farba):
    platno.itemconfig(objekt, fill=farba)

def zhasni(objekt):
    platno.itemconfig(objekt, fill="white")

def semafor():
    for i in range(10):
        rozsviet(zelena, "green")
        platno.update()
        platno.after(2000)
        zhasni(zelena)

        rozsviet(zlta, "yellow")
        platno.update()
        platno.after(1000)
        zhasni(zlta)

        rozsviet(cervena, "red")
        platno.update()
        platno.after(2000)

        rozsviet(zlta, "yellow")
        platno.update()
        platno.after(1000)
        zhasni(cervena)
        zhasni(zlta)

okno=tkinter.Tk()
okno.title("Semafor")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="white")
platno.pack()
platno.create_rectangle(50,0,250,300,fill="black")

cervena=platno.create_oval(100,0,200,100,fill="white")
zlta=platno.create_oval(100,100,200,200,fill="white")
zelena=platno.create_oval(100,200,200,300,fill="white")
semafor()

okno.mainloop()
