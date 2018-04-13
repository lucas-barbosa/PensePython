"""
Exercise 10.1

Escreva uma função chamada nested_sum que receba uma lista de listas de números
inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo: 

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""

t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
   
    t: list of list of numbers

    returns: number
    """
    total = 0
    for i in t:
        for n in i:
            total += n
    return total

print(nested_sum(t))