import turtle

def draw_sierpinski_triangle(x, y, size):
    if size <= 0:
        return
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(size)
        draw_sierpinski_triangle(x + size/2, y + size*(3**0.5)/2, size/2)
        draw_sierpinski_triangle(x - size/2, y + size*(3**0.5)/2, size/2)
        turtle.right(120)

# Wyświetl trójkąt Sierpińskiego o boku 400
turtle.setup(800, 600)
turtle.speed(1)
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.color('blue')
draw_sierpinski_triangle(0, 0, 400)
turtle.done()