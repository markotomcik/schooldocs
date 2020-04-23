import tkinter
import random

okno=tkinter.Tk()
okno.title("Bludisko")

def stvorec(x,y):
    platno.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill="blue",outline="")

def kraj():
    for i in range(32):
        if i==0 or i==31:
            for j in range(32):
                stvorec(j,i)
        else:
            stvorec(0,i)
            stvorec(31,i)

def vnutro():
    for i in range(1,31):
        for j in range(1,31):
            if random.randint(0,3)==0:
                stvorec(i,j)

def bludisko():
    platno.delete("all")    #vymaže všetky predtým nakreslené objekty na plátne
    kraj()
    vnutro()
    platno.update()         #zobrazí všetky nakreslení objekty na plátne
    
platno=tkinter.Canvas(okno, height=660, width=640, bg="white")
platno.pack()
tkinter.Button(okno,text="Generuj bludisko",command=bludisko).pack()
okno.mainloop()
