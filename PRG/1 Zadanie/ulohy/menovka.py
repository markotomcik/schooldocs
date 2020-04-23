import tkinter
okno=tkinter.Tk()
platno=tkinter.Canvas(okno, height=400, width=400, bg="white")
platno.pack()

for i in range(0, 200, 20):
    platno.create_text(100+i,100+i,fill="blue",text="Marko")

okno.mainloop()