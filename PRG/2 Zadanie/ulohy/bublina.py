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
        
okno=tkinter.Tk()
okno.title("Bublina")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
bublina_1=platno.create_oval(150-velkost/2,150-velkost/2,150+velkost/2, 150+velkost/2,fill="red")
platno.bind_all("<Key>",posun_bublinu)
okno.mainloop()

