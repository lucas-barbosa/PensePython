# Ex 4.3.1 - Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
# Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja length e então altere a chamada da função para fornecer um segundo argumento.
import turtle
import math

bob = turtle.Turtle()


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