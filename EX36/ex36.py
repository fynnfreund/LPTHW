from sys import exit

def start():
    print """
    Hello! You are in Hogwarts,
    the fantastic school of wizardry
    from the world of Harry Potter.
    The goal is to find your way to the Great Hall
    and to be sorted into your house.
    """
    print "To start the game, press ENTER."

    start_game = raw_input("> ")
    outside()

def second_hallway_r():
    print "All right, you've made through the first hallway."
    print "Now there is another junction. Left or Right?"
    print "You know the way. The ghost just told you."

    choice = raw_input("> ")

    if choice == "left":
        print "What a friendly ghost. This way is correct!"
        print "..."
        print "You are now approaching the doors of the Great Hall!"
        print "It seems like the doors are open. Great!"
        print "Do you want to enter the Great Hall?"

        choice = raw_input("> ")

        if "yes" in choice:
            great_hall()
        elif "no" in choice:
            print "What's wrong with you?"
            print "This is your last chance: Do you want to enter the Great Hall?"

            choice = raw_input("> ")

            if "yes" or "ok" in choice:
                print "Very well, I was just wondering."
                great_hall()
            else:
                dead("Ok, then you are not worthy to study wizardry at Hogwarts!")

    if choice == "right":
        print "You are following the hallway to the right."
        print "..."
        print "You are approaching a wodden door."
        print "Do you want to open it?"

        choice = raw_input("> ")

        if choice == "yes":
            dog_room()
        elif choice == "no":
            print "Seems like you don't trust the ghost, do you?"
            print "Back to the junction then."
            second_hallway_r()
        else:
            print "Yes or no?"

def dog_room():
    print "You've entered the room."
    print "Watch out!"
    print "There is a giant three-headed dog in this room. But he seems to be asleep."
    print "The bloody ghost told you the wrong way. Maybe you should've been nice to him."
    print "What do you do now?"
    print "1.) Try to leave the room as quiet as possible"
    print "2.) Try to get past the three-headed dog, as he is asleep and might not notice you."

    choice = raw_input("> ")

    if choice == "1":
        print "Lucky you! You should always be nice and greet back the ghosts you meet at Hogwarts."
        print "Back to the junction then."
        second_hallway_r()
    elif choice == "2":
        print "One of the dogs head wakes up and eats off your face."
        dead("The ghost definitly lied to you. You're a bit light-headed, aren't you?")
    else:
        print "You've got to make a decision. 1 or 2?"

def great_hall():
    print "Congrats, you've made into the Great Hall!"
    print "You've made it just in time for the Sorting Hat, who will sort you into your house!"
    print "When you're ready, press ENTER for the Sorting Hat's Song!"
    start_sorting = raw_input("> ")
    sorting()

def sorting():
    sorting_hat_song = """
    Oh you may not think I'm pretty,
    But don't judge on what you see,
    I'll eat myself if you can find
    A smarter hat than me.

    You can keep your bowlers black,
    Your top hats sleek and tall,
    For I'm the Hogwarts Sorting Hat
    And I can cap them all.

    There's nothing hidden in your head
    The Sorting Hat can't see,
    So try me on and I will tell you
    Where you ought to be.

    You might belong in Gryffindor,
    Where dwell the brave at heart,
    Their daring, nerve, and chivalry
    Set Gryffindors apart;

    You might belong in Hufflepuff,
    Where they are just and loyal,
    Those patient Hufflepuffs are true
    And unafraid of toil;

    Or yet in wise old Ravenclaw,
    if you've a ready mind,
    Where those of wit and learning,
    Will always find their kind;

    Or perhaps in Slytherin
    You'll make your real friends,
    Those cunning folks use any means
    To achieve their ends.

    So put me on! Don't be afraid!
    And don't get in a flap!
    You're in safe hands (though I have none)
    For I'm a Thinking Cap!
    """
    print "Here we go, the infamous Sorting Hat's Song!"
    print sorting_hat_song
    print "Professor McGonagall will now put the Sorting Hat onto your head."
    print "..."
    print "The Sorting Hat: 'Hello fellow Wizard! Welcome to the sorting ceremony!'"
    print "The Sorting Hat: 'In order to be sorted into your house, you have to answer the following questions.'"
    print "Press ENTER to start the sorting. Type in non-capital letters only."

    choice = raw_input("> ")

    houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']

    print "The Sorting Hat: 'Stars or Moon?'"

    choice = raw_input("> ")

    if choice == "stars" :
        print "The Sorting Hat: 'Listening or Speaking?'"
        choice = raw_input("> ")
        if choice == "listening":
            print "The Sorting Hat: 'Very intersting ...'"
            print "The Sorting Hat: 'Heart or Mind?'"
            choice = raw_input("> ")
            if choice == "heart":
                print "The Sorting Hat: 'I know it!'"
                print "The Sorting Hat: %s!!!" % houses[0]
                print "Congrats, fellow %s you finished the game!" % houses[0]
                exit(1)
            elif choice == "mind":
                print "The Sorting Hat: 'It has got to be ...'"
                print "The Sorting Hat: %s!!!" % houses[3]
                print "Congrats, fellow %s you finished the game!" % houses[3]
                exit(1)
        elif choice == "speaking":
            print "The Sorting Hat: 'Soul or Body?'"
            choice = raw_input("> ")
            if choice == "soul":
                print "The Sorting Hat: 'I know it!'"
                print "The Sorting Hat: %s!!!" % houses[0]
                print "Congrats, fellow %s you finished the game!" % houses[0]
                exit(1)
            elif choice == "body":
                print "The Sorting Hat: 'It has got to be ...'"
                print "The Sorting Hat: %s!!!" % houses[3]
                print "Congrats, fellow %s you finished the game!" % houses[3]
                exit(1)
    elif choice == "moon":
        print "The Sorting Hat: 'Earth or Sky?'"
        choice = raw_input("> ")
        if choice == "earth":
            print "The Sorting Hat: 'Intersting ...'"
            print "The Sorting Hat: 'Invisible or Almighty?'"
            choice = raw_input("> ")
            if choice == "almighty":
                print "The Sorting Hat: %s!!!" % houses[1]
                print "Congrats, fellow %s you finished the game!" % houses[1]
                exit(1)
            elif choice == "invisible":
                print "The Sorting Hat: %s!!!" % houses[3]
                print "Congrats, fellow %s you finished the game!" % houses[3]
                exit(1)
        elif choice == "sky":
            print "The Sorting Hat: 'I think I have got a clue. One more question.'"
            print "The Sorting Hat: 'Wings or Legs?'"
            choice = raw_input("> ")
            if choice == "wings":
                print "The Sorting Hat: %s!!!" % houses[2]
                print "Congrats, fellow %s you finished the game!" % houses[2]
                exit(1)
            elif choice == "legs":
                print "The Sorting Hat: %s!!!" % houses[0]
                print "Congrats, fellow %s you finished the game!" % houses[0]
                exit(1)



def right_hallway():
    print "Good choice!"
    print "..."
    print "There is a ghost in this hallway."
    print "The ghost smiles and greets you."
    print "You need to get past the ghost quickly, you are already late!"
    print "What are you going to do?"
    ghost_moved = False

    while True:
        choice = raw_input("> ")

        if "smile" in choice or "greet" in choice:
            print "Ghost: 'Good evening mister! I assume you're on the way to the Great Hall?'"
            print "Ghost: 'You need to turn left at the end of this hallway. Bless you.'"
            ghost_moved = True
            second_hallway_r()

        elif "get past" in choice or "go straight ahead" in choice or "ignore" in choice:
            print "'Ghost: Typical freshman. Always rude!'"
            print "'But anyway, I know you're late to the Sorting in the Great Hall.'"
            print "'Turn right at the end of this hallway!'"
            ghost_moved = True
            second_hallway_r()
        else:
            print "You need to do something. Smile back, greet the ghost or ignore him. Just do something, you're late!."

def left_hallway():
    print "All right. You took the left turn."
    print "..."
    print "STOP! Bloody hell! What is this?"
    print "Looks a bloody troll!"
    print "Do you flee or hide?"

    choice = raw_input("> ")

    if "flee" in choice:
        print "That's very wise! You are now on your way into the right hallway."
        right_hallway()
    elif "hide" in choice:
        dead("Well, that was stupid. The troll can smell you and will find you eventually.")
    else:
        left_hallway()


def entrance_hall():
    print "Now, you've entered Hogwarts and stand in the big entrance hall."
    print "Unfortunately there is no one to accompany you tonight."
    print "You have to find the way to the Great Hall yourself."
    print "At the end of the hallway you can either go right or left."
    print "Which way do you want to go?"

    choice = raw_input("> ")

    if choice == "right":
        right_hallway()
    elif choice == "left":
        left_hallway()
    else:
        dead("If you don't go anywhere you will be expelled.")

def dead(why):
    print why, "Goodbye!"
    exit(0)

def outside():
    print "You are outside of the Hogwarts castle"
    print "There is a heavy wodden door in front of you, which is the main entrance to the castle."
    print "Do you knock on the door just try to get in?"

    choice = raw_input("> ")

    if "knock" in choice:
        print "You better do."
        print "Well done! Mr. Filch the housekeeper will open the door for you."
        print "..."
        entrance_hall()
    elif "get in" in choice:
        print "Are you mad? This castle is full of highly skilled wizards and witches."
        print "You can't just break in. This is very rude."
        dead("Professor Dumbledore won't be happy. You will be expelled from Hogwarts.")

start()
