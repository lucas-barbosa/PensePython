"""
Exercise 10.7

Escreva uma função chamada has_duplicates que tome uma lista e
retorne True se houver algum elemento que apareça mais de uma vez.

Ela não deve modificar a lista original.
"""

def has_duplicates(s):
    t = sorted(list(s))

    for x in range(len(t) - 1):
        if t[x] == t[x+1]:
            return True
    
    return False
    
print(has_duplicates('Lucas'))
print(has_duplicates('banana'))
print(has_duplicates(['t', 'e', 's', 't', 'e']))