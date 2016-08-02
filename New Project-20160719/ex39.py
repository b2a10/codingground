# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbrevation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10 
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state,abbrev)
    
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s"  % (
            state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city


#________________________________________________#
#     Practicing dictionaries on my own here     #
#________________________________________________#

# dict for info about a country (countrysim game idea)
country = {
    'Name': 'Country 1',
    'Status': 'World Leader',
    'Attack': 4,
    'Defense': 2,
    'Terrain': 'Plains',
    'Cities': 3,
    'Ter. Size': 5,
    'Capital City': 'Capitol City',
    'Leader': 'President X',
    'Economy': 8,
    'Personality': 'Friendly'
}

# dict about the game world
world = {
    'Countries': 9,
    'World Leader': 'Country 1',
    'World President': country['Leader'],
    'Year': 4149,
    'Color': 'Red'
}

country['Governor - Cap. City'] = 'Trump'

print '-' * 10 + '\n' + '-' * 10
print "The governor of Capitol City is %s" % country['Governor - Cap. City']
print "The leader of the free world is %s" % world['World President']
print "The leading country is %s" % world[country['Status']]

print '-' * 10
print "Info about the world..."
for cat, info in world.items():
    print "The %s is %s" % (cat, info)


print '-' * 10
for status, inf in country.items():
    print "Country 1's %s is %s" % (status, inf)


# ________________________________________ #
# ________________________________________ #
# Now messing with some stuff from the pydoc #

dict1 = {
    'US': 'USA'  
}

dict2 = {
    'US': 'USA'  
}

if dict1.__cmp__(dict2) is True:
    print "Dicts are equal"

dict2['GB'] = 'Great Britain'

if dict1.__contains__('GB') is False:
    print "Correct. Dict1 does not contain \'GB\'"

dict2.__delitem__('GB')

if dict1.__eq__(dict2) is True:
    print "Correct, they should be equal"

print '-' * 10

print "The length of dict2 is %d " % dict2.__len__()

dict2.clear()
print dict1.items()

dict1['NZ'] = 'New Zealand'

dict1.iterkeys()
dict1.itervalues()
