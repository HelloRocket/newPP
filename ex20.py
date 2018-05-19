#this imports argv from the system so I can bring in a file name
from sys import argv

#this breaks the import from sys into parts and equates them to variables
script, input_file = argv

#this defines a function that will print everything in the imported file. It causes the program to print what it reads frim the imported file
def print_all(f):
    print(f.read())

#this moves the head of the reading point to the first byte.    
def rewind(f):
    f.seek(0)
    
#this tells the comouter to print a count from a variable, the curent place of the read head, and the line from that place. it removes the new line at the end
def print_a_line(line_count, f):
    print(line_count, f.tell(), f.readline(), end = "")

#this asigns the file object from the imported file to a variable                
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:\n")

current_line = 0
#print_a_line(current_line, current_file)

for i in range(3):
    current_line += 1
    print_a_line(current_line, current_file)

#current_line = current_line + 1
#print_a_line(current_line, current_file)
