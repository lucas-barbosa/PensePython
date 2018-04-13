"""
Exercise 11.1

Escreva uma função que leia as palavras em words.txt e guarde-as como chaves em um dicionário.
Não importa quais são os valores. Então você pode usar o operador in como uma forma rápida de
verificar se uma string está no dicionário.
"""


def make_dict():
    words = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        words[word] = word
    return words

def has_word(dictionary, word):
    return word in dictionary

dictionary = make_dict()
print(has_word(dictionary, 'Lucas'))
print(has_word(dictionary, 'luck'))