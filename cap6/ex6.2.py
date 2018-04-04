"""
Exercise 6.2

1.  Veja http://en.wikipedia.org/wiki/Ackermann_function. Escreva uma função
    denominada ack que avalie a função de Ackermann. Use a sua função para
    avaliar ack(3, 4), cujo resultado deve ser 125. 

2.  O que acontece para valores maiores de m e n?
"""

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

print(ack(3, 4))

# Answer 2
# There will be a infinite loop