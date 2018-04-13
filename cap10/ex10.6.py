"""
Exercise 10.6

Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra.

Escreva uma função chamada is_anagram que tome duas strings e retorne True se forem anagramas.
"""

def is_anagram(word1, word2):
    """Returns if two words is a anagram

    word1: string
    word2: string

    return: Boolean
    """
    return sorted(word1) == sorted(word2)

print(is_anagram('lucas', 'sacul'))