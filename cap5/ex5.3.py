"""
1.  Escreva uma função chamada is_triangle que receba três números
    inteiros como argumentos, e que imprima “Yes” ou “No”, dependendo
    da possibilidade de formar ou não um triângulo de gravetos com os
    comprimentos dados.

2.  Escreva uma função que peça ao usuário para digitar três comprimentos
    de gravetos, os converta em números inteiros e use is_triangle para
    verificar se os gravetos com os comprimentos dados podem formar um
    triângulo.
"""

def is_triangle(a, b, c):
    """Checks if it's a triangle

    a: first side of triangle
    b: second side of triangle
    c: third side of triangle
    """
    if a > b + c or b > a + c or c > a + b:
        print('No')
    else:
        print('Yes')

def prompting():
    a = int(input('Type a side of triangle: '))
    b = int(input('Type another side of triangle: '))
    c = int(input('Type last side of triangle: '))

    print('\nIs It a triangle?')
    is_triangle(a, b, c)

prompting()