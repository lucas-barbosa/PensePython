"""
Exercise 6.3

1.  Digite essas funções em um arquivo chamado palindrome.py e teste-as.
    O que acontece se chamar middle com uma string de duas letras? Uma letra? 
    E se a string estiver vazia, escrita com '' e não contiver nenhuma letra?

2.  Escreva uma função chamada is_palindrome que receba uma string como argumento
    e retorne True se for um palíndromo e False se não for. Lembre-se de que você
    pode usar a função integrada len para verificar o comprimento de uma string.
"""

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    """Checks if a word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('lucas'))
print(is_palindrome('ana'))
print(is_palindrome('reviver'))
print(is_palindrome('teste'))
print(is_palindrome('lol'))
print(is_palindrome('kayak'))