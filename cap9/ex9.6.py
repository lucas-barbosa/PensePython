"""
Exercise 9.6

Escreva uma função chamada is_abecedarian que retorne True se as letras numa
palavra aparecerem em ordem alfabética (tudo bem se houver letras duplas).
"""

def is_abecedarian(word):
    previous_letter = word[0]

    for letter in word:
        if ord(letter) < ord(previous_letter):
            return False
        previous_letter = letter
    return True

print(is_abecedarian('ABCDE'))
print(is_abecedarian('ABCED'))
print(is_abecedarian('ABACATE'))
print(is_abecedarian('Lopu'))