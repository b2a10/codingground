from sys import argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Exercise 13 - Study Drill 3: adding raw_input
fourth = raw_input("Name: ")

print "Your name is:", fourth