# like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# can just have arg1 and arg2
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# takes no argument
def print_none():
    print "I got nothin'."

print_two("Ben","Aronson")
print_two_again("Ben","Aronson")
print_one("First!")
print_none()