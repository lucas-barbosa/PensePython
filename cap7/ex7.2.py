"""
Exercise 7.2

A função integrada eval toma uma string e a avalia, usando o interpretador do Python.

Escreva uma função chamada eval_loop que iterativamente peça uma entrada ao usuário,
a avalie usando eval e exiba o resultado.

Ela deve continuar até que o usuário digite done.
"""

def eval_loop():
    """Shows a prompt for the user to enter a command to execute until the user types done"""
    while True:
        user_input = input('Tip a command: ')
        
        if user_input == 'done':
            break
        
        print(eval(user_input))
    return user_input

eval_loop()