# -*- coding: utf-8 -*-

# Ex 3.1 - Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:
def right_justify(s):
    print(' ' * (70 - len(s)) + s)

right_justify('Lucas')

# Ex 3.2

def do_twice(fn, val):
    fn(val)
    fn(val)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam')

def do_four(fn, val):
    do_twice(fn, val)
    do_twice(fn, val)

do_four(right_justify, 'Luke')


# Ex 3.3
def print_twice(fn):
    fn()
    fn()

def print_four(fn):
    print_twice(fn)
    print_twice(fn)
    
def simple_print(val):
    print(val, end='')

def print_border():
    do_twice(simple_print, '+----')
    print('+')

def print_content():
    do_twice(simple_print, '|    ')
    print('|')

def grid_row():
    print_border()
    print_four(print_content)

def make_grid():
    print_twice(grid_row)    
    print_border()
  
make_grid()