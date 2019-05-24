# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2  = args
    print(f'arg1: {arg1}, arg2: {arg2}')
    
# OK, that *argv is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')
    
# this just takes one argument
def print_one(arg1):
    print(f'arg1: {arg1}')
    
# this takes no argument
def print_none():
    print('I got nothing.')
    
print_two('Black', 'Red')
print_two_again('Black', 'Red')
print_one('Black')
print_none()
