# -*- coding: utf-8 -*-
"""
Exercise 7.1

Copie o loop de Raízes quadradas, na página 111, e encapsule-o em uma função chamada mysqrt
que receba a como parâmetro, escolha um valor razoável de x e devolva uma estimativa da raiz
quadrada de a.

Para testar, escreva uma função denominada test_square_root, que exibe uma tabela como esta:

a   mysqrt(a)      math.sqrt(a)   diff
-   ---------      ------------   ----
1.0 1.0            1.0            0.0
2.0 1.41421356237  1.41421356237  2.22044604925e-16
3.0 1.73205080757  1.73205080757  0.0
4.0 2.0            2.0            0.0
5.0 2.2360679775   2.2360679775   0.0
6.0 2.44948974278  2.44948974278  0.0
7.0 2.64575131106  2.64575131106  0.0
8.0 2.82842712475  2.82842712475  4.4408920985e-16
9.0 3.0            3.0            0.0

A primeira coluna é um número, a; 
A segunda coluna é a raiz quadrada de a calculada com mysqrt;
A terceira coluna é a raiz quadrada calculada por math.sqrt;
A quarta coluna é o valor absoluto da diferença entre as duas estimativas.
"""
import math

def mysqrt(number):
    """Calcules square root using Newton's method.

    number: positive integer to check square root
    """
    a = float(number) / 2
    while True:
        estimated_root = (a + number/a) / 2
        if estimated_root == a:
            return estimated_root
        a = estimated_root

def test_square_root():
    """Displays a table with result of square root"""
    line1a = 'a'
    line1b = 'mysqrt(a)'
    line1c = 'math.sqrt(a)'
    line1d = 'diff'

    mysqrt_result = []
    mathsqrt_result = []
    diff_result = []

    mysqrt_max_length = len(line1b)
    mathsqrt_max_length = len(line1c)

    for i in range(1, 10):
        mysqrt_value = mysqrt(i)
        mathsqrt_value = math.sqrt(i)
        diff = abs(mysqrt_value - mathsqrt_value)

        mysqrt_result.append(mysqrt_value)
        mathsqrt_result.append(mathsqrt_value)
        diff_result.append(diff)

        if len(str(mysqrt_value)) > mysqrt_max_length:
            mysqrt_max_length = len(str(mysqrt_value))
        
        if len(str(mathsqrt_value)) > mathsqrt_max_length:
            mathsqrt_max_length = len(str(mathsqrt_value))
    
    line1 =  line1a.ljust(4) 
    line1 += line1b.ljust(mysqrt_max_length+1) 
    line1 += line1c.ljust(mathsqrt_max_length+1)
    line1 += line1d

    line2 =  ('-'*len(line1a)).ljust(4)
    line2 += ('-'*len(line1b)).ljust(mysqrt_max_length+1)
    line2 += ('-'*len(line1c)).ljust(mathsqrt_max_length+1)
    line2 += ('-'*len(line1d))
    
    print(line1)
    print(line2)
    
    for i in range(1, 10):
        line =  str(float(i)).ljust(4)
        line += str(mysqrt_result[i-1]).ljust(mysqrt_max_length+1)
        line += str(mathsqrt_result[i-1]).ljust(mathsqrt_max_length+1)
        line += str(float(diff_result[i-1]))
        print(line)
      
test_square_root()

