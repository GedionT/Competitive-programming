import turtle

def polygon(sides: int):
    for i in range(sides):
        turtle.forward(100)
        turtle.right(360/sides)

def spaceship():
    for i in range(36):
        polygon(3)
        turtle.right(3)

def flower():
    for i in range(36):
        polygon(4)
        turtle.right(9)

flower()

spaceship()

turtle.done()
