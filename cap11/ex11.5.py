"""
Exercise 11.5

Duas palavras são “pares rotacionados” se for possível rotacionar
um deles e chegar ao outro (ver rotate_word no Exercício 8.5).

Escreva um programa que leia uma lista de palavras e encontre todos os pares rotacionados.
"""

def rotate_word(word, order):
    new_word = ''
    for letter in word:
        new_word += chr(ord(letter) + order)
    return new_word

def make_dict():
    d = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = []
    return d

def rotate_pairs(d, word):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in d:        
            d[word].append([i, rotated])
            print(word, i, rotated)

if __name__ == '__main__':
    d = make_dict()
    for word in d:
        rotate_pairs(d, word)

    for word in d:
        if d[word] != []:
            print(word, '=', d[word])
