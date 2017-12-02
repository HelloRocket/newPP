from sys import argv

script, user_name = argv
#script = argv
#script = str(script)
prompt = '> '

#print('Hi , I\'m the {} script'.format(script[125:-2]))
#print('Hi , I\'m the {} script'.format(script[-15:-2]))
print('Hi {}, I\'m the {} script'.format(user_name, script[-11:]))
print("I'd like to ask you a few questions.")
print('Do you like me {}'.format(user_name))
likes = input(prompt)

print('Where do you live {}'.format(user_name))
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print('''Alright, so you said {} about liking me.
And you live in {}. Not sure where that is.
And you have a {} computer. Nice
'''.format(likes, lives, computer))

