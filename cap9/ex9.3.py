"""
Exercise 9.3

Escreva uma função chamada avoids que receba uma palavra e uma série de letras
proibidas, e retorne True se a palavra não usar nenhuma das letras proibidas.

Altere o código para que o usuário digite uma série de letras proibidas e o
programa imprima o número de palavras que não contêm nenhuma delas. Você pode
encontrar uma combinação de cinco letras proibidas que exclua o menor número
possível de palavras?
"""

def avoids(word, invalid_letters):
    """ Checks if word not contains any forbidden letter

    word: string to check
    invalid_letters: forbidden
    """
    for letter in invalid_letters:
        if letter in word:
            return False
    return True

invalid_letters = input('Digite as letras proibidas: ')

fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if avoids(word, invalid_letters):
        count += 1

print(count)