"""
Exercise 10.5

Escreva uma função chamada is_sorted que tome uma lista como parâmetro e retorne True se
a lista estiver classificada em ordem ascendente, e False se não for o caso. Por exemplo:

>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
"""

def is_sorted(t):
    """ Returns if a list is sorted

    t: list

    returns: Boolean
    """
    # Best code
    return t == sorted(t)
    # My code
    for i in range(len(t)):
        if i == 0:
            continue
        if t[i] < t[i-1]:
            return False
    return True
        
print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))