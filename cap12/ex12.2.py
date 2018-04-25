"""
Exercise 12.2

Mais anagramas!

Escreva um programa que leia uma lista de palavras de um arquivo (veja “Leitura de listas de 
palavras”, na página 133) e imprima todos os conjuntos de palavras que são anagramas.

    Aqui está um exemplo de como a saída pode parecer:

    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']

    Dica: você pode querer construir um dicionário que mapeie uma coleção de letras a uma lista
    de palavras que podem ser soletradas com essas letras. A pergunta é: como representar a
    coleção de letras de forma que possa ser usada como uma chave?

Altere o programa anterior para que exiba a lista mais longa de anagramas
primeiro, seguido pela segunda mais longa, e assim por diante.

No Scrabble, um “bingo” é quando você joga todas as sete peças na sua estante, junto com uma peça
no tabuleiro, para formar uma palavra de oito letras. Que coleção de oito letras forma o maior
número possível de bingos? Dica: há sete.

"""
def sort_word(word):
    """ Returns a sorted word

    word: string
    return: string
    """
    return ''.join(sorted(word))

def all_anagram(filename):
    """ Makes a anagrams dictionary

    filename: string
    return: dictionary
    """
    d = {}
    fin = open(filename)
    for line in fin:
        word = line.strip().lower()
        k = sort_word(word)
        d.setdefault(k, []).append(word)
    return d

def order_by_length(d, reverse):
    """ Order dictionary by length

    d: dictionary
    reverse: bool
    return: list
    """
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    t.sort(reverse=reverse)
    return t

def filter_by_length(d, n):
    """ Filter anagrams by length of word

    d: string
    n: int
    return: dictionary
    """
    res = {}
    for key, anagrams in d.items():
        if len(key) == n:
            res[key] = anagrams
    return res

def print_by_length(t):
    for x in order_by_length(t, False):
        print(x)

if __name__ == '__main__':
    anagrams = all_anagram('words.txt')
    print_by_length(anagrams)

    eigth_letters = filter_by_length(anagrams, 8)
    print_by_length(eigth_letters)