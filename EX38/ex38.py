ten_things = "Apples Oranges Pinapples Mobile Sugar Water"

print "Wait, what the fuck? There are not 10 things, you savage! Let us fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Gin", "Tonic", "Lemon"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we Go: "; stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # omfg
print stuff.pop()
print ' '.join(stuff) #wtf
print '#'.join(stuff[3:5]) #whuuaaat
