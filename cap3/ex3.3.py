# Ex 3.3
def do_twice(fn):
    fn()
    fn()

def do_four(fn):
    do_twice(fn)
    do_twice(fn)

def print_border():
    print(('+' + '-' * 4) * 2 + '+')

def print_row():
    print(('|' + ' ' * 4) * 2 + '|')

def grid_content():
    print_border()
    do_four(print_row)

def make_grid():
    do_twice(grid_content)
    print_border()
  
make_grid()