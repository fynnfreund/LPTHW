print "You enter a dark room with two dors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating peanutbutter jam sandwiches. What do you do?"
    print "1. Try to nick the peanutbutter jam sandwiches and run."
    print "2. Scream at the bear."
    print "3. Tell the bear that the peanutbutter jam sandwich belogs to you."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats you legs off. Good job."
    elif bear == "2":
        print "The bear eats your face off. Great job."
    elif bear == "3":
        print "The bear tells you to get the fuck of here."
        print "You have to options:"
        print "1. Do as he says."
        print "2. Tell him you love him and just want to cuddle."

        options = raw_input("> ")

        if options == "1":
            print "You're leaving the room. The bear wishes you a good day."
        else:
            print "The bear is emotionally touched and says 'Sharing is caring! Let us cuddle!'."
    else:
        print "Well. doing %s is probably better. Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yeling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "You body survives powered by a mind of a jellyfish. Well done."

    else:
        print "The insanity rots your eyes into a pool of mick. Excellent!"

else:
    print "You stumble around and fall on a knife and die. Good job, mate."
