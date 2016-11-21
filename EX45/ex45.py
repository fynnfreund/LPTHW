# 'The Ancient Mysteries'
# a game by Fynn Freund

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        exit(1)



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('final')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Intro(Scene):

    def enter(self):
        print """
            Hello, and welcome to 'The Ancient Mysteries'.
            This is a riddle-game, set in the City of London.
            The goal is to find and unlock the legend of the ancient mysteries,
            which is some sort of treasure that holds the lost wisdom of the forgotten ages
            and has the power to change the world.
            On your way you will encounter several puzzles that are not always easy.
            Pay attention to the details and hints!
            Use Google if you are stuck. Type in all non-capital letters.

            Good luck!
            """
        print "[Press ENTER to start the game]"
        go = raw_input()
        return 'westminster_bridge'

class Failed(Scene):

    endings = [
        "You are not worthy. You will never find the ancient mysteries. Game over.",
        "Seems like you are unqualified. Try it again in a few years maybe. Bye.",
        "Well, well, well, if it was that easy, everyone could do it. You've failed.",
        "This is about the ancient mysteries, serious stuff you know. Nice try.",
    ]

    def enter(self):
        print Failed.endings[randint(0, len(self.endings)-1)]
        exit(1)

class WestminsterBridge(Scene):

    def enter(self):
        print "Tonight is a special night."
        print "A prophesy predicted the ancient mysteries to be found and unveiled, tonight ... here in the city of London."
        print "I know, you are a very famous professor and symbolist, but it won't be easy."
        print "Legend says, that the ancient mysteries are somewhere buried in London."
        print "What will be found at the bottom has to power to completely change the world."
        print "Rumor has it, that it is some sort of source, which contains the lost wisdom of the forgotten age."
        print " ... but it is written in an ancient language, which can only be read by very few people on earth."
        print " "
        print "You are standing on Westminster Bridge."
        print "An old friend of yours once told you, that all mysteries start with politics."
        print "You see the dimly lit Parliament of London. Where will you go?"

        direction = raw_input("> ")

        if "parliament" in direction:
            return 'parliament'
        else:
            print "Pay attention to the details!"
            print "An old friend of yours once told you, that all mysteries start with politics."
            print "Where will you go?"

            direction = raw_input("> ")

            if "parliament" in direction:
                return 'parliament'
            else:
                return 'failed'

class Parliament(Scene):

    def enter(self):
        print " "
        print "You're entering the famous and glorious Parliament of London."
        print "Legend says, that the ancient mysteries can only be found with a map that points the way."
        print "But where in hell would you find a map in the Parliament of London?"
        print "Your mobile phones rings! Answer it?"

        answer = raw_input("> ")

        if "yes" in answer:
            print " "
            print "A deep voice cracks through the speaker."
            print ' "Hello Professor. It is not of your concern who I am." '
            print ' "Fact is, you are the choosen one. You, only you can find and unveil the ancient mysteries tonight." '
            print ' "It happens that I know how to find the map to points the way." '
            print ' "And as this is matter of national security, I want you to trust me." '
            print ' "To find the map, one simply needs to look towards the burned heaven of lodge 1097, it will lead the way." '
            print "The man hangs up."
            print "Where do you go?"

            answer = raw_input("> ")

            if "lodge" in answer or "1097" in answer:
                print "Yes, seems obvious, but there is no lodge 1097 in the parliament."
                print "..."
                print "You are suddenly having a flash and no exaclty where to find the map."
                print "The oldest part of the Parliament was built in 1097."
                print "Although this part burned down in 1834, one small lodge was still intact."
                print "Go there?"

                choice = raw_input("> ")

                if "yes" in choice:
                    return 'lodge_1097'
                else:
                    print "This is the only possible idea you have. You failed already."
                    return 'failed'
            else:
                print "Pay attention to the details!"
                print "'One simply needs to look towards the burned heaven of lodge 1097, it will lead the way.''"
                print "Where will you go?"

                choice = raw_input("> ")

                if "lodge" in choice or "1097" in choice:
                    print "Yes, seems obvious, but there is no lodge 1097 in the parliament."
                    print "..."
                    print "You are suddenly having a flash and no exaclty where to find the map."
                    print "The oldest part of the Parliament was built in 1097."
                    print "Although this part burned down in 1834, one small lodge was still intact."
                    print "Go there?"

                    choice = raw_input("> ")

                    if "yes" in choice:
                        return 'lodge_1097'
                    else:
                        print "This is the only possible idea you have. You failed already."
                        return 'failed'
                else:
                    print "This is the only possible idea you have. You failed already."
                    return 'failed'
        else:
            print "You have no bloody idea how to find a map in this building."
            print "Maybe you should have answered that call."
            return 'failed'

class Lodge1097(Scene):

    def enter(self):
        print "..."
        print "You found your way to the old lodge."
        print "Where do you find the map?"
        print "You still hear the mans voice in your head:"
        print "'One simply needs to look towards the burned heaven of lodge 1097, it will lead the way.'"
        print "Where do you look?"

        look = raw_input("> ")

        if "heaven" in look or "up" in look or "ceiling" in look:
            print " "
            print "You've got a realy sharp mind, Professor."
            print " "
            print "You're looking up towards the ceiling and find a giant painting."
            print "On the painting you see a great bridge with a small, weird looking pyramid beneath it,"
            print "just like the one on the one-dollar note."
            print "Is that supposed to be a map? Doesn't look like one, does it?"
            print "Maybe it merely tells you about the place where you can find the map."
            print "What famous bridge in London do you know?"

            answer = raw_input("> ")

            if "towerbridge" in answer or "tower bridge" in answer:
                print " "
                print "Excatly. Tower Bridge it must be!"
                print "Tower Bridge is only a couple of minutes away on the tube."
                print "Circle or District Line from Embankment to Tower Hill. Hurry!"
                print "[Press ENTER to continue]"
                go = raw_input()
                return 'tower_bridge'
            else:
                return 'failed'
        else:
            return 'failed'

class TowerBridge(Scene):

    def enter(self):
        print " "
        print "You've made to Tower Bridge. Beautiful, isn't it?"
        print "But we not here to admire or take selfies in front of it."
        print "This is a matter of national security, the man said."
        print "Where would you look in order to find the map?"
        print "Remember, the painting on the ceiling potrayed a small pyramid beneath the bridge."
        print "A pyradmid has always been a symbol for mysteries, no?"
        print "You've heard of small little chambers down inside the bridges collumns. But could it be?"
        print "Where do you go?"

        choice = raw_input("> ")

        if "inside" in choice or "chambers" in choice or "chamber" in choice or "collumn" in choice:
            print " "
            print "Yes, that's the only clue we have, isn't it?"
            print "..."
            print "You are making your way inside the first collumn of Tower Bridge."
            print "There is a locked door with keypad."
            print "The code is 4 digits."
            print "Think! Didn't the man on your mobile tell you a 4 digit number earlier?"
            code = "1097"
            guess = raw_input("[keypad]> ")
            guesses = 9

            while guess != code and guesses >= 1:
                print "[keypad]: Wrong. %d guesses left." % guesses
                guesses -= 1
                guess = raw_input("[keypad]> ")

            if guess == code:
                print "[CLICK] "
                print "The door clicks and swings open."
                print "There is a staircase that leads down into the collumn."
                print "You're going down. Your heart's pounding."
                print "..."
                print "After 5min of descend you've reached the bottom. A dark round room with a single pillar in the middle."
                print "What you find takes your breath."
                print "So the legend is true?"
                print "This is more serious than you expected."
                print " "
                print "On the pillar in the middle of the room sits a small pyramid with a flat top."
                print "You have a closer look at it and find an engraving on the surface of the flat top."
                print "You slowly understand: The 'map' was never a real map, it was just a symbol. The actual map is this pyramid."
                print "But how does it point the way to the ancient mysteries?"
                print "And why doies the pyramid have a flat top? The capstone is missing..."
                print " "
                print "You're trying to read the engravings:"
                print "[Press ENTER to read the engravings]"
                go = raw_input()
                print """
                         i
                         O
                        [o]
                        The legend will be found at the 33rd degree -> */\*
                        """
                print "[Press ENTER to continue]"
                go = raw_input()
                print "You have no idea what i O [o] means ..."
                print "'33rd degree' ... hmmm."
                print "What could '-> */\*' mean, though?"
                print """
                        Let's think:
                        -> = direction = go to
                        ** = star = sacred = church
                        /\ = top = view = high
                        """
                print "You start to understand: The legend will be found at a sacred, high viewpoint in London."
                print " "
                print "Where do you go?"

                place = raw_input("> ")

                if "stpauls" in place or "st. paul's" in place or "cathedral" in place:
                    print " "
                    print "Yes, it must be the infamous St. Paul's Cathedral of London."
                    print "Not too far from here. Hurry!"
                    print "[Press ENTER to continue]"
                    go = raw_input()
                    return 'st_pauls'
                else:
                    print "Come on. Think!"
                    print "What's a famous church in London?"

                    place = raw_input("> ")

                    if "stpauls" in place or "st. paul's" in place or "cathedral" in place:
                        print " "
                        print "Yes, it must be the infamous St. Paul's Cathedral of London."
                        print "Not too far from here. Hurry!"
                        print "[Press ENTER to continue]"
                        go = raw_input()
                        return 'st_pauls'
                    else:
                        return 'failed'

            else:
                print "[keypad]: No guesses left. Door will be locked for ever."
                print "You've failed."
                return 'failed'

        else:
            print "Where else would you go?"
            raw_input("> ")
            return 'failed'

class StPauls(Scene):

    def enter(self):
        print " "
        print "You've made to St. Paul's Cathedral."
        print "*/\* can only point to the viewing gallery of the dome. It used to be the highest point in London."
        print "You're going up to St. Paul's viewing platform."
        print "..."
        print "You're walking round the viewing gallery wondering if this the right place"
        print "as thousands of tourist come here every day,"
        print "when something the catches your eye ..."
        print "A small symbol on the wall:"
        print """
                [o]
                """
        print "[Press ENTER to continue]"
        go = raw_input()
        print " "
        print "You slowly realise where you've seen this symbol before."
        print "You take another look at the pyramid in your bag and your assumption confirms itself."
        print "You're having a closer look at the symbol on the wall and notice"
        print "that it is actully engraved on some sort of disc build into the dome's wall."
        print "You wonder if it is moveable."
        print "You remember:'The legend will be found at the 33rd degree'"
        print " "
        print "What do you do?"

        choice = raw_input("> ")

        if "33 degree" in choice or "rotate" in choice:
            print " "
            print "The disc disappears into the wall and leaves a small round hole."
            print "What do you do?"

            choice = raw_input("> ")

            if "grab" in choice or "inside" in choice or "insert" in choice:
                print " "
                print "Your finger touch a cool, small object."
                print "It feels like ... wait ... no, that can't be."
                print "..."
                print "You pull your hand out."
                print "In your hand lies an even smaller pyramid. Made out of solid gold."
                print "Wait: So this is the legend of the ancient mysteries? The wisdom of the forgotten world?"
                print "No .. and slowly you start to understand."
                print "'This must be the missing capstone!''"
                print " "
                print "On the golden capstone you find very delicate engravings:"
                print """
                    i commemorates the Great Fire of London
                    O takes one from earth to heaven and reverse
                    """
                print " "
                print "Where do you go?"
                print "If you don't understand yet, take another look at the pyramid (type pyramid)."

                answer = raw_input("> ")

                if "monument" in answer:
                    print " "
                    print "Yes, great! The Monument to the Great Fire of London, a Doric column not far from here, commemorates the Great Fire of London."
                    print "This must be the place!"
                    print "[Press ENTER to continue]"
                    go = raw_input()
                    return 'monument'
                else:
                    print """
                         i
                         O
                        [o]
                        The legend will be found at the 33rd degree -> */\*
                        """
                    print "The capstone is not THE legend. It is A legend. A Legend to read the map, to decipher the pyramid."
                    print "'i commemorates the Great Fire of London'"
                    print "What place commemorates the Great Fire of London?"

                    answer = raw_input("> ")

                    if "monument" in answer:
                        print "Yes, excellent! The Monument to the Great Fire of London, a Doric column not far from here, commemorates the Great Fire of London."
                        print "This must be the place!"
                        print "Well done, you're on your way to the Monument."
                        print "[Press ENTER to continue]"
                        go = raw_input()
                        return 'monument'
                    else:
                        return 'failed'
            else:
                print "Try again!"
                print "[Press ENTER to try again]"
                go = raw_input()
                return 'st_pauls'
        else:
            return 'failed'



class Monument(Scene):

    def enter(self):
        print " "
        print "You have arrived at the The Monument to the Great Fire of London."
        print "There is only one last puzzle to solve."
        print "You have the map and the legend."
        print """
             i - solved that: The Monument
             O - 'takes one from earth to heaven and reverse.' hmm ...
            [o] - hmmm ...

            """
        print " "
        print " 'O takes one from earth to heaven and reverse.' "
        print "Think more specific:"
        print "How do you ascend and descend a building like the Monument?"
        print "Hint: It takes a lot of steps..."

        answer = raw_input("> ")

        if "stairs" in answer or "staircase" in answer:
            print "Excatly! Now have a look inside the Monument:"
            print "There is a spiral staircase inside that takes you up to the top of the collumn."
            print "But take another a look at the map."
            print "[Press ENTER to look at the pyramid]"
            go = raw_input()
            print """
                 i - The Monument
                 O - Spiral Staircase
                [o]
                """
            print "[Press ENTER to continue]"
            go = raw_input()
            print "'[o]' must be the symbol for the ancient mysteries."
            print "Up or down?"

            choice = raw_input("> ")

            if choice == "up":
                print "Really? Think again."
                print """
                     i - The Monument
                     O - Spiral staircase
                    [o] - The Ancient Mysteries
                    """
                print "Up or down?"

                choice = raw_input("> ")

                if choice == "down":
                    print "Yes, according to the map the ancient mysteries must be beneath the Monument!"
                    print "And there must be another spiral staircase going down!"
                    print "[Press ENTER to continue]"
                    go = raw_input()
                    return 'final'
                else:
                    return 'failed'
            elif choice == "down":
                print "Yes, according to the map the ancient mysteries must be beneath the Monument!"
                print "And there must be another spiral staircase going down!"
                print "[Press ENTER to continue]"
                go = raw_input()
                return 'final'
            else:
                return 'failed'
        else:
            return 'failed'

class Final(Scene):

    def enter(self):
        print " "
        print "You are now inside at the base of the Monument."
        print "But there is no staircase going down. Only the one going up."
        print "..."
        print "Wait ... there is a small hatch in the floor."
        print "There is an old rusty combination lock on it."
        print "The code is 8 digits!"
        print "There is a poem engraved on the back of the lock:"
        print "[Press ENTER to read the poem]"
        go = raw_input()
        print """
            Sparks from a baker's oven
            Set the blaze with hellish fury
            Timbers dry from sweltering summer
            House after house bursting into flame.
            """
        print "[Press ENTER to continue]"
        go = raw_input()
        print "The code must have something to do with the great fire of London!"
        print "8 digits ... could be a historic date, no?"
        print "What's the code?"
        code="02111666"
        guesses = 9

        guess = raw_input("> ")

        while guess != code and guesses >= 1:
            print "Try again."
            guesses -= 1
            guess = raw_input("> ")

        if guess == code:
            print "The lock clicks and opens."
            print "Well done! You've solved everything!"
            print "You can now go down the staircase to unleash the ancient mysteries."
            print "Do you really want to do this?"

            choice = raw_input("> ")

            if choice == "yes":
                print " "
                print "Have fun! But don't destroy the world."
                print "You won!"
                exit(1)
            else:
                print " "
                print "Ok, very wise .. maybe it is better not to."
                print "You won!"
                exit(1)
        else:
            print "That's enough. You will never make it."
            return 'failed'



class Map(object):

    scenes = {
        'intro': Intro(),
        'westminster_bridge': WestminsterBridge(),
        'parliament': Parliament(),
        'lodge_1097': Lodge1097(),
        'tower_bridge': TowerBridge(),
        'st_pauls': StPauls(),
        'monument': Monument(),
        'final': Final(),
        'failed': Failed(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('intro')
a_game = Engine(a_map)
a_game.play()
