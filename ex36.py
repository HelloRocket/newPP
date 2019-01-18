from sys import exit
from random import choice, randint

#The Great Baby Adventure by bigTanuki

def start():
    print('''Today is a busy day. You need to take care of your little baby daughter. You are at home. Everything is good.
    Suddenly, you babydaughter starts to cry.''')
    first_choice()

def first_choice(): 
    print('What do you do?')
    print('Do you ignore her, pick her up or turn on the TV?')
    
    do_what = input('> ')
    print(do_what)
    
    if 'ignore' in do_what or 'turn' in do_what:
        print('She cries louder')
        
        first_choice()
        
    elif 'pick' in do_what:
        print('She smells stinky!')
        poop_smell()
        
    elif 'magic' in do_what:
        print('She stops crying. Everything is fine. Good job. You win!')
        exit(0)
        
    else:
        print('That does not help.')
        first_choice()
        
        
def poop_smell():
    exit(0)
    
start()
