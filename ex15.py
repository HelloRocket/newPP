#this imports file name and oher info into the program
from sys import argv
#this defines variables that hold the arg values we imported
script, filename = argv

#this creates a file object with the text contents from the refered file
txt = open(filename)
#prints a string woth the imported file name
#print('Here is your file {}:'.format(argv[1]))
print(f'Here is your file {filename}:')
#extracts the text content from the file object and then prints it to screen
print(txt.read())

print('Type the filename again:')
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())

