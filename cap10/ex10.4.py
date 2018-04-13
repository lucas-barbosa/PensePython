"""
Exercise 10.4

Escreva uma função chamada chop que tome uma lista alterando-a para
remover o primeiro e o último elementos, e retorne None. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
"""

def chop(t):
    """Removes the first and last of t

    t: list
    """
    t.pop(0)
    t.pop()

t = [1, 2, 3, 4]
chop(t)
print(t)