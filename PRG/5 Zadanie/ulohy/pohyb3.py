import tkinter
import math

velkost=2

def pohybuj_loptickou():
    for i in range(1,280):
        x=i
        y = 10*math.sqrt(x)
        platno.create_oval(x,y,x+velkost,y+velkost,fill="black")
        platno.coords(lopticka,x,y,x+velkost,y+velkost)
        platno.update()
        platno.after(10)
        
okno=tkinter.Tk()
okno.title("Pohyb")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="white")
platno.pack()
lopticka=platno.create_oval(0,0,velkost,velkost,fill="black")
pohybuj_loptickou()
okno.mainloop()

