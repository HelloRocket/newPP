from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

input(f"The input file is {len(indata)} bytes long. Does {to_file} exist?  {exists(to_file)}. Press return to continue.")

out_file = open(to_file, 'w')
out_file.write(indata)

print(f"Copied from {from_file} to {to_file}")
out_file.close()
