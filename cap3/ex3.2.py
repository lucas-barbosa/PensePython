# Ex 3.2
def print_spaced(word):
    print('----' + word + '----')

def do_twice(fn, val):
    fn(val)
    fn(val)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_spaced, 'spam')

def do_four(fn, val):
    do_twice(fn, val)
    do_twice(fn, val)

do_four(print_spaced, 'Luke')