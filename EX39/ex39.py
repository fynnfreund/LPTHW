# create a mapping of state to abbreaviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print states
# create a basic set of status and some cities in them
cities = {
    'CA': 'San Fransicsco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print all cities, included the added ones.
print cities
#print out some cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the sate then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print "-" * 10
for state, abbrev in states.items():
    print "%s has the city %s" % (state, abbrev)

# print every city in state
print "-" * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print "-" * 10
for stae, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])


print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('New York')
print "This should be NY: ", state
state = states.get('Texas')

if not state:
    print "Sorry, no Texas. (Because they suck.)"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
