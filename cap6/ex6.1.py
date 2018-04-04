"""
Exercise 6.1

1.  Desenhe um diagrama da pilha do seguinte programa. 
    O que o programa exibe?

"""

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))

# Answer 1
'''

__main__:
    x --> 1
    y --> 2

c:
    x --> 1
    y --> 5
    z --> 3
    total --> 9
    square --> 0

b:
    z --> 9
    prod --> 0

a:
    x --> 9
    y --> 9
    x --> 10

b:
    z --> 9
    prod --> 90


c:
    x --> 1
    y --> 5
    z --> 3
    total --> 9
    square --> 8100

'''