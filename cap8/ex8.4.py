"""
Exercise 8.4

As seguintes funções pretendem verificar se uma string contém alguma letra minúscula,
mas algumas delas estão erradas. Para cada função, descreva o que ela faz (assumindo 
que o parâmetro seja uma string).
"""

def any_lowercase1(s):
    # Checks only first letter in string if it's lower, returning a boolean
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    # Checks if string 'c' is lower and returns string 'True'
    # It never returns false, because 'c' is always lower.
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    # Checks all letters in string if it's lower and keep in a variable called flag
    # Returns only last letter all the time
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    # Checks if any letter in word is lower and return a boolean
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    # Checks if every letter in string is uppercase
    for c in s:
        if not c.islower():
            return False
    return True


