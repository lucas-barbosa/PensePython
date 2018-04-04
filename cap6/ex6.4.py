"""
Exercise 6.4

1.  Um número a é uma potência de b se for divisível por b e a/b for uma potência
    de b. Escreva uma função chamada is_power que receba os parâmetros a e b e
    retorne True se a for uma potência de b. Dica: pense no caso-base.
"""

def is_power(a, b):
    """Checks if a number is power of another
    
    a: power
    b: integer
    """
    if a == b:
        return True
    if a % b != 0:
        return False
    return is_power(a/b, b)
