# Ex 4.3.2 - Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados.
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

polygon(bob, 90, 5)
polygon(bob, 95, 6)
polygon(bob, 100, 7)