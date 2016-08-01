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

"""
Function to assign seeds randomly to teams
"""
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
        seeded[index][0] = seeds[index]
        seeded[index][1] = shuff_teams[index]       

    return seeded


"""
Set up "match arrays" based on seeds. 
Currently hardcoded for only 4 or 8teams
"""
def setup_bracket(teamlist, num_lines):
    if num_lines == 4:
        print "four teams"
        cols, rows = 2, 2
        matches = [[0 for x in range(cols)] for y in range(rows)]
        
        end = num_lines-1
        for i in range(num_lines/2):
            matches[i][0] = teamlist[i]
            matches[i][1] = teamlist[end]
            end = end-1
        return matches
    else:
        print "eight teams"
        cols, rows = 2, 4
        matches = [[0 for x in range(cols)] for y in range(rows)]
        
        # need to test this
        end = num_lines-1
        for i in range(num_lines/2):
            matches[i][0] = teamlist[i]
            matches[i][1] = teamlist[end]
            end = end-1
        return matches

"""
Function to run a sim through a 'match.'
In the future, add all matches to an array and return for user access
"""
def match_game(matchups, match_num):
    if match_num == "C":
        team1 = matchups[0]
        team2 = matchups[1]
    else:
        team1 = matchups[match_num][0]
        team2 = matchups[match_num][1]
    
    # Function returns true if Team 1 has lower seed, false if Team 2 does
    hi_seed = higher_seed(team1[0], team2[0])
    
    # THE KEY TO GETTING RID OF THE UGLINESS OF THE STRINGS!!!!!
    t1str = team1[1].replace("\n","")
    t2str = team2[1].replace("\n","")    
    
    # Lower seed gets advantage
    if hi_seed is True:
        # Team 1 has lower seed
        t1num = random.randint(1,50) * 1.25
        t2num = random.randint(1,50)
        
        if t1num > t2num:
            print "The %s defeat the %s, %d to %d" % (t1str, t2str, t1num,t2num)
            return team1
        else:
            print "Upset! The %s defeat the %s, %d to %d" % (t2str, 
                        t1str, t2num, t1num)
            return team2
    else:
        # Team 2 has lower seed
        t1num = random.randint(1,50)
        t2num = random.randint(1,50) * 1.25
        
        if t1num > t2num:
            print "The %s defeat the %s, %d to %d" % (t1str, t2str, t1num,t2num)
            return team1
        else:
            print "Upset! The %s defeat the %s, %d to %d" % (t2str, 
                        t1str, t2num, t1num)
            return team2
        
    

"""
Function to determine which team has lower seed in a match. 
Will return True if Team 1 (seed1) has a lower seed, False if Team 2 is lower.
"""
def higher_seed(seed1, seed2):
    if seed1 < seed2:
        return True
    else:
        return False


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

# Sort teams by their seeds
final_seeds.sort()

for k in range(0,num_lines):
    print final_seeds[k]

# need to account for more than 4 teams here 
cols, rows = 2, 2  
bracket = [[0 for x in range(cols)] for y in range(rows)] 

# Call function to set up matches - aka bracket
bracket = setup_bracket(final_seeds, num_lines)

for l in range(0,2):
    print bracket[l]


# Play the matches - second arg is which match number to be played
w1 = match_game(bracket, 0)
w2 = match_game(bracket, 1)

win1 = w1[1].replace("\n","")
win2 = w2[1].replace("\n","")   

print "The championship game is: %d %s versus %d %s" % (w1[0], win1, w2[0],win2)

nround = []
nround.append(w1)
nround.append(w2)

c = match_game(nround, "C")

champ = c[1].replace("\n","")
print "The %d %s are the champions!" % (c[0], champ)

















