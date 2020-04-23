import tkinter

velkost=20

def opeciatkuj_cervenou(udalost):
    x=udalost.x
    y=udalost.y
    platno.create_line(x-velkost/2,y-velkost/2,x+velkost/2, y+velkost/2)
        
okno=tkinter.Tk()
okno.title("Bublina")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
platno.bind("<B1-Motion>",opeciatkuj_cervenou)
okno.mainloop()

