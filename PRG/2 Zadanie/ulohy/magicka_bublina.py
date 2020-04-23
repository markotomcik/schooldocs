import tkinter
import random

velkost=100
farby=["red","blue","green","yellow","pink"]

def zmen_bublinu(udalost):
    klaves=udalost.keysym
    if klaves == "w":
        color="white"
    elif klaves == "b":
        color="blue"
    elif klaves == "space":
        color=random.choice(farby)

    platno.itemconfig(bublina,fill=color)
        
okno=tkinter.Tk()
okno.title("Bublina")
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
bublina=platno.create_oval(150-velkost/2,150-velkost/2,150+velkost/2, 150+velkost/2,fill="red")
platno.bind_all("w",zmen_bublinu)
platno.bind_all("b",zmen_bublinu)
platno.bind_all("<space>",zmen_bublinu)
okno.mainloop()

