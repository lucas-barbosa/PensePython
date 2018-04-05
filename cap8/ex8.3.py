"""
Exercise 8.3

Uma fatia de string pode receber um terceiro índice que especifique o “tamanho do passo”;
isto é, o número de espaços entre caracteres sucessivos. Um tamanho de passo 2 significa
tomar um caractere e outro não; 3 significa tomar um e dois não etc.

>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'

Um tamanho de passo -1 atravessa a palavra de trás para a frente, então a fatia [::-1]
gera uma string invertida.

Use isso para escrever uma versão de uma linha de is_palindrome do Exercício 6.3.
"""

def is_palindrome(word):
    """Checks if a word is an palindrome
    
    word: string to check
    """
    return word == word[::-1]

print(is_palindrome('Lucas'))
print(is_palindrome('ana'))