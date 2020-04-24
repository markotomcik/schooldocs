import tkinter

nasobok = 1 
rychlost = 500 # pxps (kilopixel za sekundu)
framerate = 50 # fps 

def prelet():
    for i in range(int(1100/rychlost*framerate)):
        platno.move(raketa,int(nasobok*rychlost/framerate),0)
        platno.update()
        platno.after(int(1000/framerate))

okno=tkinter.Tk()
okno.title("Raketa")    
platno=tkinter.Canvas(okno, height=300, width=1000, bg="black")
platno.pack()
obrazok=tkinter.PhotoImage(file = 'raketa.gif')
raketa=platno.create_image(-75, 100, image = obrazok, anchor = "nw")
prelet()
platno.create_text(500, 150, text="KONIEC", fill="white", font=("Helvetica", 150))
   
okno.mainloop()
