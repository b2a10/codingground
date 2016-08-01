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
|  that contains an EVEN number of team names
|-You will use this as the argument required when
|  running the program 'ex36.py'
"""
#_______________________________#

# function definitions # 
def seed_assign(shuff_teams):

    cols, rows = 2, 4
    seeded = [[0 for x in range(cols)] for y in range(rows)]

    index = 0
    for index in range(0,4):
        seeded[index][0] = shuff_teams[index]       
        seeded[index][1] = random.randint(1,4)

    return seeded

    
    




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
final_seeds = seed_assign(shuffled)

for k in range(0,num_lines):
    print final_seeds[k]












