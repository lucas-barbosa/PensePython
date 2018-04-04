"""
Exercise 5.2.
O último teorema de Fermat diz que não existem números inteiros a, b e c
tais que:

    a**n + b**n == c**n

para quaisquer valores de n maiores que 2.

1.  Escreva uma função chamada check_fermat que receba quatro parâmetros – 
    a, b, c e n – e verifique se o teorema de Fermat se mantém. Se n for maior
    que 2 e 
        
        a**n + b**n == c**n 
        
    o programa deve imprimir, “Holy smokes, Fermat was wrong!” Senão o programa
    deve exibir “No, that doesn’t work.”

2.  Escreva uma função que peça ao usuário para digitar valores para a, b, c e n,
    os converta em números inteiros e use check_fermat para verificar se violam o
    teorema de Fermat.
"""

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')

def prompting():
    a = input('Type your value of a: ')
    b = input('Type your value of b: ')
    c = input('Type your value of c: ')
    n = input('Type your value of n: ')

    check_fermat(int(a), int(b), int(c), int(n))

prompting()