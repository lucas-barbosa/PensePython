"""
Exercise 11.2

Leia a documentação do método de dicionário setdefault e
use-o para escrever uma versão mais concisa de invert_dict.
"""

def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

print(invert_dict({'a': 5, 'b': 5, 'c': 3, 'd': 8}))
