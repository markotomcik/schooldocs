import turtle
import numpy
import random
tabula=turtle.Screen()
pero=turtle.Turtle()
pero.hideturtle()
pero.width(5)
for strana in range(4):
    pero.color("#"+("%06x"%random.randint(0,16777215)))
    pero.forward(50)
    pero.right(90)
tabula.mainloop()
