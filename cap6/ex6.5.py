"""
Exercise 6.5

1.  Escreva uma função chamada gcd que receba os parâmetros
    a e b e devolva o maior divisor comum.
"""

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

print(gcd(16, 8))
print(gcd(140, 25))