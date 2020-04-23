import tkinter

velkost=20

def opeciatkuj_cervenou(udalost):
    x=udalost.x
    y=udalost.y
    if x < 150:
        if y < 150:
            color="yellow"
        else:
            color="blue"
    else:
        if y < 150:
            color="green"
        else:
            color="red"
    platno.create_oval(x-velkost/2,y-velkost/2,x+velkost/2, y+velkost/2,fill=color)
        
okno=tkinter.Tk()
okno.title("Bublina")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="lightgray")
platno.pack()
platno.bind("<Button-1>",opeciatkuj_cervenou)
okno.mainloop()

