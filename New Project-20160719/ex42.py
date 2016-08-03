## Animal is-a object (yes, sort of confusing) look at extra credit
class Animal(object):
    pass

## Dog is an Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has a name
        self.name = name

## Cat is an Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## Cat has a name
        self.name = name
    
## Person is an object
class Person(object):
    
    def __init__(self, name, language):
        ## Person has a name
        self.name = name
        
        ## Person has a pet of some kind
        self.pet = None
        self.language = language
    
    def says_hello(self):
        if self.language == "english":
            print "%s says hello" % self.name
        elif self.language == "spanish":
            print "%s says hola" % self.name
        elif self.language == "german":
            print "%s says hallo" % self.name
        else:
            print "%s says yo" % self.name
        
## Employee is a person
class Employee(Person):
    
    def __init__(self, name, salary, language):
        ## Employee has a name
        super(Employee, self).__init__(name, language)
        ## Emplyee has a salary
        self.salary = salary
        
        
    

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
## -- skip --

## rover is a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary", "english")
mary.says_hello()

## mary has a pet that is satan
mary.pet = satan

## frank is an employee that has a name "frank" and has a salary 120000
frank = Employee("Frank", 120000, "spanish")
frank.says_hello()

## frank has a pet that is rover
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
#harry = Halibut()











