import tkinter
import random

LED = []

def blikaj():
    while True:
        platno.itemconfig(random.choice(LED), fill="#"+("%06x"%random.randint(0,16777215)))
        platno.update()
        platno.after(random.randint(0, 1000))

okno=tkinter.Tk()
okno.title("Svetlá")    
platno=tkinter.Canvas(okno, height=300, width=300, bg="gray")
platno.pack()
LED.append(platno.create_oval(10,180,50,280,fill="white"))
LED.append(platno.create_oval(70,180,110,280,fill="white"))
LED.append(platno.create_oval(130,180,170,280,fill="white"))
LED.append(platno.create_oval(190,180,230,280,fill="white"))
LED.append(platno.create_oval(250,180,290,280,fill="white"))
for i in range(5):
    platno.create_rectangle(20+i*60,300,40+i*60,270,fill="black")
blikaj()
   
okno.mainloop()
