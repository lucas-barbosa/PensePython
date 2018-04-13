"""
Exercise 10.2

Escreva uma função chamada cumsum que receba uma lista de números e retorne
a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma
dos primeiros i+1 elementos da lista original. Por exemplo:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]

"""

def cumsum(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers
    """
    total = 0
    result = []
    for i in t:
        total += i
        result.append(total)
    return result

t = [1, 2, 3]
print(cumsum(t))
