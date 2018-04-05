"""
Exercise 9.2

Escreva uma função chamada has_no_e que retorne True
se a palavra dada não tiver a letra “e” nela.
"""

def has_no_e(word):
    """Checks if a word not contains letter 'e'"""
    return not 'e' in word

fin = open('words.txt')
without_e = 0
total = 0

for line in fin:
    word = line.strip()
    total += 1
    if has_no_e(word):
        without_e += 1
        print(word)

print(str(100 * without_e/total) + '%')
