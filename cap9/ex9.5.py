"""
Exercise 9.5

Escreva uma função chamada uses_all que receba uma palavra e uma série de letras
obrigatórias e retorne True se a palavra usar todas as letras obrigatórias pelo
menos uma vez. 
"""
def uses_all(word, letters):
    for letter in letters:
        if not letter in word:
            return False
    return True

print(uses_all('Lucas', 'lck'))    
print(uses_all('Teste', 'ts'))