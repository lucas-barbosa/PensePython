"""
Exercise 10.9

Escreva uma função que leia o arquivo words.txt e construa uma lista com um elemento por palavra.

Escreva duas versões desta função, uma usando o método append e outra usando a expressão t = t + [x]. 

Qual leva mais tempo para ser executada? Por quê?
"""
from time import time

def by_append():
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def by_expression():
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t

start_time = time()
t = by_append()
elapsed_time = time() - start_time

print("Time Elapsed by Append: ", elapsed_time)

start_time = time()
t = by_expression()
elapsed_time = time() - start_time

print("Time Elapsed by Expression: ", elapsed_time)