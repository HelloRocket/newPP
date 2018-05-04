# this one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# ok, *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# this just takes 1 argument
def print_one(arg1):
    print(f"arg1: {arg1}")
    
# this one takes no arguments
def print_none():
    print('I got nothing.')
    
    
print_two('justin', 'barrera')
print_two_again('justin', 'barrera')
print_one('one more')
print_none()
