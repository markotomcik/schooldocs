import tkinter

velkost=20

def pohybuj_loptickou():
    for i in range(10):
       platno.move(lopticka,0,10)
       print(platno.coords(lopticka)) 
       platno.update()
       platno.after(100)
    for i in range(10):
       platno.move(lopticka,0,-10)
       print(platno.coords(lopticka)) 
       platno.update()
       platno.after(500)
        
okno=tkinter.Tk()
okno.title("Pohyb")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
lopticka=platno.create_oval(150-velkost/2,150-velkost/2,150+velkost/2, 150+velkost/2,fill="red")
pohybuj_loptickou()
okno.mainloop()

