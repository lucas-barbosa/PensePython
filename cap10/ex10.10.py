"""
Exercise 10.10

Para verificar se uma palavra está na lista de palavras, você pode usar o
operador in, mas isso seria lento porque pesquisaria as palavras em ordem.

Como as palavras estão em ordem alfabética, podemos acelerar as coisas com uma busca por
bisseção (também conhecida como pesquisa binária), que é semelhante ao que você faz quando
procura uma palavra no dicionário. Você começa no meio e verifica se a palavra que está
procurando vem antes da palavra no meio da lista. Se for o caso, procura na primeira metade
da lista. Se não, procura na segunda metade.

De qualquer forma, você corta o espaço de busca restante pela metade.
Se a lista de palavras tiver 113.809 palavras, o programa seguirá
uns 17 passos para encontrara palavra ou concluir que não está lá.

Escreva uma função chamada in_bisect que receba uma lista ordenada, um valor-alvo
e devolva o índice do valor na lista se ele estiver lá, ou None se não estiver.
"""

def read_file():
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def in_bisect(t, word):
    i = len(t)

    if i == 0:
        return 'There is not words on list.'
    
    i = i // 2

    if t[i] == word:
        return i
    
    first_index = 0
    if word > t[i]:
        first_index = i+1
        t = t[first_index:]
    else:
        t = t[:i]

    for i in range(len(t)):
        if t[i] == word:
            return first_index + i
    
    return 'Word is not on file!'

            
t = read_file()
print(in_bisect(t, 'luck'))
print(in_bisect(t, 'Lucas'))