"""Community Manager Game"""
import ex45info
from sys import exit
from random import randint


class Engine(object):
    
    def __init__(self, hood, morale):
       self.hood = hood
       self.morale = morale
    
    def play(self):
        pass

class Morale(object):
    
    morale = 0
    
    #def __init__(self):
    #    pass
    
    def increase(self):
        self.morale+=1
        return self.morale
    
    def decrease(self):
        self.morale-=1
        return self.morale

class Project(object):
    
    def create(self):
        print "This project is not yet configured. Subclass it and implement create()."
        exit(1)

class Fundraiser(Project):
    
    fund = 0
    
    def create(self):
        print "Fundraiser Creator\n-------------\nChoose a fundraiser:"
        for i in range(1,len(ex45info.fundraisers)+1):
            print "%d. %s" % (i, ex45info.fundraisers.get(i))
        
        print "Enter the number of your choice"
        self.fund = int(raw_input("> "))
        response = 0
        
        if self.fund == 4 or self.fund == 7 or self.fund == 8:
            print "Nobody likes this idea. No money raised and no morale boosted."
            response = 0
            return response
        else: 
            print "Great idea! Morale boosted and money raised."
            reponse = 1
            return response



class Initiative(Project):
    
    initiat = 0
    
    def create(self):
        print "Initiative Creator\n-------------\nChoose an initiative:"
        for i in range(1,len(ex45info.initiatives)+1):
            print "%d. %s" % (i, ex45info.initiatives.get(i))
        
        print "Enter the number of your choice"
        self.initiat = int(raw_input("> "))
        response = 0
        
        if self.initiat == 1 or self.initiat == 6 or self.initiat == 8:
            print "Nobody likes this idea. No money raised and no morale boosted."
            response = 0
            return response
        else: 
            print "Great idea! Morale boosted and money raised."
            reponse = 1
            return response

class Build(Project):
    
    building = 0
    cost = 0
    
    def create(self):
        print "Building Creator\n----------\nChoose a building:"
        for i in range(1,len(ex45info.builds)+1):
            print "%d. %s - $%d" % (i, ex45info.builds.get(i), 
                                    ex45info.costs.get(ex45info.builds.get(i)))
        
        print "Enter the number of your choice"
        self.building = int(raw_input("> "))
        self.cost = ex45info.costs.get(ex45info.builds.get(self.building))
        response = 0
        
        # check money

class Neighborhood(object):
    
    Months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    current_month = Months[0]
    years = 0
    cash = 0
    
    def __init__(self, start_month):
        self.start_month = start_month

    def next_month(self):
        self.current_month +=1
        print self.current_month
        return self.current_month
    
    def increase_year(self):
        self.years += 1
        return self.years
        
    def incr_cash(self, event):
        if isinstance(event, Fundraiser):
            if event.fund == 1 or event.fund == 6:
                print "made 20"
                self.cash +=20
            elif event.fund == 3:
                print "made 40"
                self.cash +=40
            elif event.fund == 2 or event.fund == 5:
                print "made 100"
                self.cash +=100
            else:
                print "no money made"
    
    def decr_cash(self, event):
        if isinstance(event, Initiative):
            if event.initiat == 1 or event.initiat == 5 or event.initiat == 4:
                print "lost 20"
                self.cash -=20
            elif event.initiat == 3 or event.initiat == 8:
                print "lost 40"
                self.cash -=40
            elif event.initiat == 2 or event.initiat == 6 or event.initiat == 7:
                print "lost 100"
                self.cash -=100
        elif isinstance(event, Build):
            cost = event.cost
            print "lost %d" % cost
            self.cash -=cost
    
a_hood = Neighborhood(1)
morally = Morale()

fr = Fundraiser()
#fr.create()

ini = Initiative()
#ini.create()

bld = Build()
bld.create()

#a_hood.incr_cash(fr)
#a_hood.decr_cash(ini)
#a_hood.decr_cash(bld)
#print a_hood.cash

a_game = Engine(a_hood, morally)
a_game.play()




