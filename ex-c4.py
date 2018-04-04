import turtle
import math

bob = turtle.Turtle()

# Ex 4.3.1 - Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
# Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja length e então altere a chamada da função para fornecer um segundo argumento.

def square(t, length):
    """Draws a square.

    t: Turtle
    length: length of the sides
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 25)
square(bob, 40)
square(bob, 65)
square(bob, 80)

# Ex 4.3.2 - Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados.

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

# Ex 4.3.3 - Escreva uma função chamada circle que use o turtle t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados.

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)

circle(bob, 100)

arc(bob, 50, 30)
turtle.mainloop()

