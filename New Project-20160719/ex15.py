# import argv from sys module in order to accept arguments
from sys import argv

# take in script file and text file as argument
script, filename = argv

# open passed in text file
txt = open(filename)

# read the text file which will display it
print "Here's your file %r:" % filename
print txt.read()

txt.close()

# ask user to type in filename again
print "Type the filename again:"
file_again = raw_input("> ")

# open the file again, and below this; read it and display
txt_again = open(file_again)

print txt_again.read()

txt_again.close()
