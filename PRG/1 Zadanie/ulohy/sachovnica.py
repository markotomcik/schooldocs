import tkinter
okno=tkinter.Tk()
platno=tkinter.Canvas(okno, height=640, width=640, bg="black")
platno.pack()

def stvorec(x,y,color="white"):
    platno.create_rectangle(x,y,x+80,y+80,fill=color,outline="")

for y in range(8):
    for x in range(8):
        if y%2==0:
            if x%2==0:
                stvorec(x*80,y*80)
        else:
            if x%2==1:
                stvorec(x*80,y*80)

okno.mainloop()