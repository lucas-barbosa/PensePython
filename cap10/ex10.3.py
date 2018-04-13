"""
Exercise 10.3

Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com
todos os elementos originais, exceto os primeiros e os últimos elementos. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]

"""

def middle(t):
    """Returns a list without first and last index

    t: list
    
    returns: new list
    """
    return t[1:-1]

t = [1, 2, 3, 4]
print(middle(t))