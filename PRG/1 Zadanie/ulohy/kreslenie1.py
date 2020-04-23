import tkinter
okno=tkinter.Tk()
platno=tkinter.Canvas(okno, height=600, width=600, bg="lightblue")
platno.pack()

platno.create_rectangle(0,500,600,600,fill="green",outline="")
platno.create_rectangle(100,300,300,500,fill="darkred",outline="")
platno.create_rectangle(150,350,250,400,fill="white",outline="")
platno.create_polygon(100,300,300,300,200,150,fill="red",outline="")
platno.create_oval(450,50,550,150,fill="yellow",outline="")

okno.mainloop()
