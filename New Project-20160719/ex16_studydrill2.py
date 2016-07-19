from sys import argv

script, filename = argv

print "About to access file..."
file = open(filename)

print "About to display file..."
print file.read()

print "About to close file..."
file.close()