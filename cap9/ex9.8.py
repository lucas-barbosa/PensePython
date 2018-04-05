"""
Exercise 9.8

“Estava dirigindo outro dia e percebi algo no hodômetro que chamou a minha atenção.
Como a maior parte dos hodômetros, ele mostra seis dígitos, apenas em milhas inteiras.
Por exemplo, se o meu carro tivesse 300.000 milhas, eu veria 3-0-0-0-0-0.

“Agora, o que vi naquele dia foi muito interessante. Notei que os últimos 4 dígitos
eram um palíndromo; isto é, podiam ser lidos da mesma forma no sentido correto e no
sentido inverso. Por exemplo, 5-4-4-5 é um palíndromo, então no meu hodômetro poderia
ser 3-1-5-4-4-5.

“Uma milha depois, os últimos 5 números formaram um palíndromo. Por exemplo, poderia
ser 3-6-5-4-5-6. Uma milha depois disso, os 4 números do meio, dentro dos 6, formavam
um palíndromo. E adivinhe só? Um milha depois, todos os 6 formavam um palíndromo!

“A pergunta é: o que estava no hodômetro quando olhei primeiro?”

Escreva um programa Python que teste todos os números de seis dígitos e imprima
qualquer número que satisfaça essas condições.
"""

def is_palindrome(word):
    return word == word[::-1]

def check(number):
    if is_palindrome(str(number)[2:]):
        number += 1
        if is_palindrome(str(number)[1:]):
            number += 1
            if  is_palindrome(str(number)[1:5]):
                number += 1
                if is_palindrome(str(number)[1:5]):
                    return True
    return False
    

for i in range(100000, 999999):
    if check(i):
        print(i)