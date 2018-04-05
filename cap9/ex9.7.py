"""
Exercise 9.7

Dê uma palavra com três letras duplas consecutivas. Vou dar exemplos de 
palavras que quase cumprem a condição, mas não chegam lá:

Por exemplo, a palavra committee, c-o-m-m-i-t-t-e-e. 
Seria perfeita se não fosse aquele ‘i’ que se meteu ali no meio. 

Ou Mississippi: M-i-s-s-i-s-s-i-p-p-i.
Se pudesse tirar aqueles ‘is’, daria certo. 

Mas há uma palavra que tem três pares consecutivos de letras e, que eu
saiba, pode ser a única palavra que existe. É claro que provavelmente
haja mais umas 500, mas só consigo pensar nessa. 

Qual é a palavra?
"""

def check_consecutive(word):
    i = 0
    count = 0

    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count += 1
            i += 2
            if count == 3:
                return True
        else:
            count = 0
            i += 1
    return False

def print_consecutive():
    fin = open('words.txt')

    for line in fin:
        word = line.strip()
        if check_consecutive(word):
            print(word)

print('Here are all the words that have three consecutives double letters: ')
print(print_consecutive())
print('')
