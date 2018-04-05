"""
Exercise 9.4

Escreva uma função chamada uses_only que receba uma palavra e uma série
de letras e retorne True, se a palavra só contiver letras da lista. 

Você pode fazer uma frase usando só as letras acefhlo?
Que não seja “Hoe alfalfa?”
"""

def uses_only(word, letters):
    """ Checks if a word uses only letter in letters

    word: string to check
    letters: allowed letters
    """
    for letter in word:
        if not word in letters:
            return False
    return True

print(uses_only('Lucas', 'Lucas'))    
print(uses_only('Teste', 'ts'))