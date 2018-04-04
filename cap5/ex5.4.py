"""
Exercise 5.4

1.  Qual é a saída do seguinte programa? Desenhe um diagrama da pilha 
    que mostre o estado do programa quando exibir o resultado.

2.  O que aconteceria se você chamasse esta função desta forma:
    recurse(-1, 0)?    

3.  Escreva uma docstring que explique tudo o que alguém precisaria
    saber para usar esta função (e mais nada).

"""

def recurse(n, s):
    """Recursive function to getting and printing the value of s
       
    n: positive integer
    s: integer
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

# Answer1:

'''

__main__:
    None

recurse:
    n --> 3
    s --> 0

recurse:
    n --> 2
    s --> 3

recurse:
    n --> 1
    s --> 5

recurse:
    n --> 0
    s --> 6

'''

# Answer2:
# There would be an infinite loop, because the parameter n never would be zero.