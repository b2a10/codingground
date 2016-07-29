# this is my own idea of practice after having not practiced
# python in a week or so. working with lists and taking input

i = 0
listerine = []

print "How many items do you use to clean your teeth?"

items = int(raw_input("> "))

print "So you use %d items to clean your teeth. What are they?" % items

for i in range(0,items):
    objecto = raw_input("> ")
    listerine.append(objecto)

print "Ok, so you use ",
for strng in listerine:
    print "%s, " % strng,
print "to clean your teeth"