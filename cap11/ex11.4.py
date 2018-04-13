"""
Exercise 11.4

Se fez o Exercício 10.7, você já tem uma função chamada has_duplicates, que recebe uma lista
como parâmetro e retorna True se houver algum objeto que aparece mais de uma vez na lista.

Use um dicionário para escrever uma versão mais rápida e simples de has_duplicates.
"""

def has_duplicates(t):
    d = {}
    for i in t:
        if i in d:
            return True
        d[i] = 1
    return False


t = ['Lucas', 'Débora', 'Luana', 'Leonardo', 'Miguel', 'Luana', 'Pedro', 'Luan', 'Débora', 'Débora']
print(has_duplicates(t))