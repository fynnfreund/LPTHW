from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a lot of peanut butter."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take peanut butter":
            dead("The bear looks at you and the slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear says that you're very tasty looking and starts to chew on your leg.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def crappy_room():
    print "Here you see a bunch of crap."
    print "The crap is starting to form into a crap-monster and goes insane."
    print "Do you flee for you life or eat your hand?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "hand" in choice:
        dead("Well that was tasty!")
    else:
        crappy_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        crappy_room()
    else:
        dead("You stumble around the until you die painfully, you savage!")


start()
