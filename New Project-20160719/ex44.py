# implicit inheritance
class Parent(object):
    
    def implicit(self):
        print "PARENT implicit()"
    
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# override explicitly
class Parent2(object):
    
    def override(self):
        print "PARENT override()"

class Child2(Parent):
    
    def override(self):
        print "CHILD override()"

dad2 = Parent2()
son2 = Child2()

dad2.override()
son2.override()

# alter before or after
class Parent3(object):
    
    def altered(self):
        print "PARENT altered()"

class Child3(Parent3):
    
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child3, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad3 = Parent3()
son3 = Child3()

dad3.altered()
son3.altered()


# all three combined
class Parent4(object):
    
    def override(self):
        print "PARENT override()"
        
    def implicit(self):
        print "PARENT implicit()"
    
    def altered(self):
        print "PARENT altered()"

class Child4(Parent4):
    
    def override(self):
        print "CHILD overrid()"
        
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child4, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad4 = Parent4()
son4 = Child4()

dad4.implicit()
son4.implicit()

dad4.override()
son4.override()

dad4.altered()
son4.altered()


# composition
class Other(object):
    
    def override(self):
        print "OTHER override()"
        
    def implicit(self):
        print "OTHER implicit()"
    
    def altered(self):
        print "OTHER altered()"
    
class Child0(object):
    
    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print "CHILD override()"
    
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son0 = Child0()

son0.implicit()
son0.override()
son0.altered()


