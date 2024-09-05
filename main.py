import turtle

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("lightblue")
turtleScreen.title("CicekApi")
turtleIstance = turtle.Turtle()
turtleIstance.color("red")
def leaf():
    turtleIstance.circle(100, 60)
    turtleIstance.left(120)
    turtleIstance.circle(100, 60)
    turtleIstance.left(120)
def flower():
    leaf()
    turtleIstance.right(60)

for i in range(6):
    flower()
turtleIstance.color("blue")
turtleIstance.right(90)
turtleIstance.forward(200)

turtle.mainloop()



