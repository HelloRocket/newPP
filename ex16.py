from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")

print("If you want to do that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating this file. Goodbye!")
target.truncate()

print("Now I am going to ask you for 3 lines.")

line1 = input('Line 1: ')
line2 = input('Line 2: ')
line3 = input('Line 3: ')

print("I'm going to write these to a file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And finally, we close it.')
target.close()