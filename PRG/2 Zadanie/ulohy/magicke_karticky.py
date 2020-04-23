import tkinter
import random

velkost=50
farby=["red","blue","green","yellow","pink"]

def zmen_farbu(udalost):
    x=udalost.x
    y=udalost.y
    color="#"+("%06x"%random.randint(0,16777215))

    if 100-velkost < y < 100+velkost:
        if 100-velkost/2 < x < 100+velkost/2:
            platno.itemconfig(karta_1,fill=color)
        elif 200-velkost/2 < x < 200+velkost/2:
            platno.itemconfig(karta_2,fill=color)
        elif 300-velkost/2 < x < 300+velkost/2:
            platno.itemconfig(karta_3,fill=color)
        
okno=tkinter.Tk()
okno.title("Magické kartičky")    
platno=tkinter.Canvas(okno, height=200, width=400, bg="lightgray")
platno.pack()
platno.create_text(200,25,text="Klikni na kartičku, aby si zmenil jej farbu!")
karta_1=platno.create_rectangle(100-velkost/2,100-velkost,100+velkost/2, 100+velkost,fill="white")
karta_2=platno.create_rectangle(200-velkost/2,100-velkost,200+velkost/2, 100+velkost,fill="white")
karta_3=platno.create_rectangle(300-velkost/2,100-velkost,300+velkost/2, 100+velkost,fill="white")
platno.bind_all("<Button-1>", zmen_farbu)
okno.mainloop()

