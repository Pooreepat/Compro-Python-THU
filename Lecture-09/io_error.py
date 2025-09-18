filename = input('Enter a filename: ')
try:
    infile = open(filename,'r')
    contents = infile.read()
    print(contents)
    infile.close()
except IOError:
    print('An error occured rrying to read')
    print('the file',filename)

print("End of the Program")