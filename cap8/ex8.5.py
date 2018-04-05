# Exercise 8.5

def rotate_word(word, order):
    """Encrypt given word using Ceasar cypherand given swift"""
    new_word = ''
    for letter in word:
        new_word += chr(ord(letter) + order)
    return new_word

print(rotate_word('cheer', 7))
print(rotate_word('HAL', 1))