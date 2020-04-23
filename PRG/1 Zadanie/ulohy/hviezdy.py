import tkinter
import random
okno=tkinter.Tk()
okno.title("Hviezdna obloha")

def obloha():
    platno.delete("all")    #vymaže všetky predtým nakreslené objekty na plátne
    
    for i in range(random.randint(50, 100)):
        x = random.randint(0, 300)
        y = random.randint(0, 300)
        p = random.randint(1, 5)
        platno.create_oval(x, y, x+p, y+p, fill="white", outline="")

    platno.update()         #zobrazí všetky nakreslení objekty na plátne
    
platno=tkinter.Canvas(okno, height=300, width=300, bg="black")
platno.pack()
tkinter.Button(okno,text="Generuj oblohu",command=obloha).pack()
okno.mainloop()

