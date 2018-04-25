"""
Exercise 12.1

Escreva uma função chamada most_frequent que receba uma string e exiba as letras
em ordem decrescente de frequência. Encontre amostras de texto de vários idiomas
diferentes e veja como a frequência das letras varia entre os idiomas. 

Compare seus resultados com as tabelas em http://en.wikipedia.org/wiki/Letter_frequencies.
"""

def most_frequent(s):
    histogram = make_histogram(s)
    t = []
    for key, value in histogram.items():
        t.append((value, key))
    
    t.sort(reverse=True)

    res = []
    for key, value in t:
        res.append(value)
    
    return res

def make_histogram(s):
    d = {}
    for x in s:
        d[x] = d.setdefault(x, 0) + 1
    return d
    
if __name__ == '__main__':
    seq = most_frequent('lucasias')
    for x in seq:
        print(x)