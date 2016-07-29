"""
This file is dedicated to trying to create a more 'complicated'
program after completing over half of the exercises from
Zed Shaw's "Learn Python the Hard Way.' The idea is to foster
some creative thinking and using some of the simple stuff I've 
learned so far. -BA
"""

# Silly Puzzle
print "Welcome to \"Silly Puzzle\"!"
print "Select Easy or Hard difficulty: "
answer = raw_input("> ")

if answer == "Easy":
    print "Easy. Decipher a three-letter word."
    print " __  __  __ "
    print "Press ENTER to continue to the next letter"
    ent = raw_input("> ")
    print "Letter 1 - A letter that is volumtuous and curvy. Makes you think of something that stings or something naughty."
    
    b = False
    while b is False: 
        let1 = raw_input("> ")
        
        if(let1 == "B" or let1 == "b"):
            print "Correct -- B __ __"
            b = True
        else:
            print "Incorrect. Try again"
    
    print "Letter 2 - When you see something disgusting, you might mention this letter. It can be small, but can start something big (like a large mammal)."
    
    e = False
    while e is False: 
        let2 = raw_input("> ")
        
        if(let2 == "E" or let2 == "e"):
            print "Correct -- B e __"
            e = True
        else:
            print "Incorrect. Try again"
            
    print "Letter 3 - I'm tired of typing this, the letter finishes my name."
    let3 = raw_input("> ")
    if(let3 == "N" or let3 == "n"):
        print "Correct -- B e n"
    else:
        print "C'mon man!"
else:
    "I am tired of typing this game and don't feel like making a Hard difficulty, deal with it."


"""
Alright, here's the deal. This started as a great idea and I ought to do this for more practice but I've spent almost two years doing this stuff. I'm just going to keep going with the exercises and maybe I'll come back when I have a better idea for a program to build. Just don't want to write a text based simple program.
"""