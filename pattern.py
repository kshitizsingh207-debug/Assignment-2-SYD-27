import turtle

t = turtle.Turtle()
t.speed(0)          
t.width(2)          
t.color("black")

screen = turtle.Screen()
screen.bgcolor("white")

def draw_edge(length, depth):

    if depth == 0:
        t.forward(length)
        return

    part = length / 3

    draw_edge(part, depth - 1)

    t.right(60)

    draw_edge(part, depth - 1)

    t.left(120)

    draw_edge(part, depth - 1)

    t.right(60)

    draw_edge(part, depth - 1)

sides = int(input("Enter the number of sides: "))
length = int(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

angle = 360 / sides

for _ in range(sides):
    draw_edge(length, depth)
    t.right(angle)

turtle.done()
