import turtle
import math

bob = turtle.Turtle()

def polygon(t, length, n):
    """Draws a polygon

    t: Turtle
    length: length of the sides
    n: sides number
    """
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# Ex 4.3.3 - Escreva uma função chamada circle que use o turtle t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados.

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)

circle(bob, 100)

turtle.mainloop()

