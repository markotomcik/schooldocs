import tkinter

velkost=20

def posun_bublinu(udalost):
    klaves=udalost.keysym
    if klaves=="Left":
        platno.move(bublina_1,-10,0)
    elif klaves=="Right":
        platno.move(bublina_1,10,0)
    elif klaves=="Up":
        platno.move(bublina_1,0,-10)
    elif klaves=="Down":
        platno.move(bublina_1,0,10)
    elif klaves=="a":
        platno.move(bublina_2,-10,0)
    elif klaves=="d":
        platno.move(bublina_2,10,0)
    elif klaves=="w":
        platno.move(bublina_2,0,-10)
    elif klaves=="s":
        platno.move(bublina_2,0,10)
    elif klaves=="space":
        platno.delete("all")
        okno.destroy()

okno=tkinter.Tk()
okno.title("Bublina")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
bublina_1=platno.create_oval(130-velkost/2,150-velkost/2,130+velkost/2, 150+velkost/2,fill="red")
bublina_2=platno.create_oval(170-velkost/2,150-velkost/2,170+velkost/2, 150+velkost/2,fill="blue")
platno.bind_all("<Key>",posun_bublinu)
okno.mainloop()

