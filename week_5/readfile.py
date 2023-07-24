import fileinput
# This will continue until the end of file (EOF)
for line in fileinput.input():
    print(line)
# Executed by 'python readfile.py names.txt'

# This takes the extra line away
for line in fileinput.input():
    print(line, end='')
