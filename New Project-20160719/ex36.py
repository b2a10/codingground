"""
Exercise 36: Creating my own game.
|-Bracket-type game
"""

from sys import argv
import datetime
import random

today = datetime.date.today()
print today
gameday = datetime.datetime(2016,07,30,12,30)
print "The game will be played at %s EST" % gameday.__str__()

#_______________________________#
"""
Bracket Game
|-Please create a .txt file named 'teamdb.txt'
|  that contains either 4 or 8 teams
|-You will use this as the argument required when
|  running the program 'ex36.py'
"""
#_______________________________#

# function definitions # 

# function to assign seeds randomly to teams 
def seed_assign(shuff_teams, num_lines):

    cols, rows = 2, num_lines
    seeded = [[0 for x in range(cols)] for y in range(rows)]
    seeds = []
    
    for r in range(0,num_lines):
        contains = False
        while contains is False:
            rand_seed = random.randint(1,num_lines)
            
            if not seeds.__contains__(rand_seed):
                seeds.append(rand_seed)
                contains = True

    for index in range(0,num_lines):
        seeded[index][0] = shuff_teams[index]       
        seeded[index][1] = seeds[index]

    return seeded

def sort_seeds(shuffled, num_lines):
    sorted_seeds = []
    
    while sorted_seeds.__len__() != 4:
        print "hey"


def setup_bracket(pool, num_lines):
    if num_lines == 4:
        print "four teams"
        match1 = []
        match2 = []
        
    else:
        print "eight teams"

    
    




# begin rest of program #

script, teamdb = argv

teams = open(teamdb)

# Holds the team data from teamdb.txt
teamdata = teams.read()

i = 0
num_lines = sum(1 for line in open(teamdb))
teampool = []

# Adds each time on its own line to the team pool list
with open(teamdb) as file:
    for line in file:
        teampool.append(line)

# print each team being used 
for i in range(0,num_lines):
    print teampool[i],


# creating new list for randomly shuffled teams
shuffled = []

print "---Seeded---"

# shuffles the team pool into a new list - see pydoc for '9.6 random'
shuffled = random.sample(teampool, num_lines)

for j in range(0,num_lines):
    print shuffled[j],

final_seeds = []
final_seeds = seed_assign(shuffled, num_lines)

for k in range(0,num_lines):
    print final_seeds[k]

#setup_bracket(num_lines)

sort_seeds(shuffled, num_lines)









