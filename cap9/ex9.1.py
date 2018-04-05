"""
Exercise 9.1

Escreva um programa que leia words.txt e imprima apenas as 
palavras com mais de 20 caracteres (sem contar whitespace).
"""
fin = open('words.txt')

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
