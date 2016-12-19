class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
welcome = Scene("Welcome to 'The Ancient Mysteries'", "welcome",
"""
This is a riddle-game, set in the City of London.
The goal is to find and unlock the legend of the ancient mysteries,
which is some sort of treasure that holds the lost wisdom of the forgotten ages
and has the power to change the world.
On your way you will encounter several puzzles that are not always easy.
Pay attention to the details and hints!
Use Google if you are stuck or type in "help" if you need a little hint ;-)
Type in all non-capital letters.

Good luck!

Start the game?
""")

westminster_bridge = Scene("Westminster Bridge", "westminster_bridge",
"""
Tonight is a special night.
A prophesy predicted the ancient mysteries to be found and unveiled, tonight ... here in the city of London.
I know, you are a very famous professor and symbolist, but it won't be easy.
Legend says, that the ancient mysteries are somewhere buried in London.
What will be found at the bottom has to power to completely change the world.
Rumor has it, that it is some sort of source, which contains the lost wisdom of the forgotten age.
 ... but it is written in an ancient language, which can only be read by very few people on earth.

You are standing on Westminster Bridge.
An old friend of yours once told you, that all mysteries start with politics.
You see the dimly lit Parliament of London. Where will you go?

Type "help" if you need a hint.
""")

hint_1 = Scene("Help", "hint_1",
"""
Pay attention to the details!
An old friend of yours once told you, that all mysteries start with politics."
Where will you go?
"""
)

parliament = Scene("In the Parliament", "parliament",
"""
You're entering the famous and glorious Parliament of London.
Legend says, that the ancient mysteries can only be found with a map that points the way.
But where in hell would you find a map in the Parliament of London?
Your mobile phones rings! Answer it?
""")

phone_call = Scene("Phone Call", "phone_call",
"""
A deep voice cracks through the speaker.
"Hello Professor. It is not of your concern who I am."
"Fact is, you are the choosen one. You, only you can find and unveil the ancient mysteries tonight."
"It happens that I know how to find the map to points the way."
"And as this is matter of national security, I want you to trust me."
"To find the map, one simply needs to look towards the burned heaven of lodge 1097, it will lead the way."
The man hangs up.
Where do you go?

Type "help" if you don't know yet.
""")

hint_2 = Scene("Help", "hint_2",
"""
Maybe there is some kind of lodge no. 1097 in the parliament ...?
Where do you go?
""")

lodge_1097 = Scene("In Lodge 1097", "lodge_1097",
"""
You found your way to the old lodge.
Where do you find the map?
You still hear the mans voice in your head:
'One simply needs to look towards the burned heaven of lodge 1097, it will lead the way.'
Where do you look?

Type "help" if you need a hint.
""")

hint_3 = Scene("Help", "hint_3",
"""
What could be an analogy to heaven?
What direction do you look, when you look into the sky or heaven?
""")

ceiling = Scene("The 'Heaven' of Lodge 1097", "ceiling",
"""
You've got a realy sharp mind, Professor.

You're looking up towards the ceiling and find a giant painting.
On the painting you see a great bridge with a small, weird looking pyramid beneath it,
just like the one on the one-dollar note.
Is that supposed to be a map? Doesn't look like one, does it?
Maybe it merely tells you about the place where you can find the map.
What famous bridge in London do you know?
""")

tower_bridge = Scene("At Tower Bridge", "tower_bridge",
"""
You've made to Tower Bridge. Beautiful, isn't it?

But we not here to admire or take selfies in front of it.
This is a matter of national security, the man said.
Where would you look in order to find the map?
Remember, the painting on the ceiling potrayed a small pyramid beneath the bridge.
A pyradmid has always been a symbol for mysteries, no?
You've heard of small little chambers down inside the bridges collumns. But could it be?
Where do you go?

Type "help" if you don't know yet.
""")

hint_4 = Scene("Help", "hint_4",
"""
There are indeed little chambers down inside Tower Bridges collums.
Go there?
""")

inside_tower_bridge = Scene("Inside Tower Bridge", "inside_tower_bridge",
"""
Yes, that's the only clue we have, isn't it?

You are making your way inside the first collumn of Tower Bridge.
There is a locked door with keypad.
The code is 4 digits.
Think! Didn't the man on your mobile tell you a 4 digit number earlier?

Type "help" if you need a hint.
""")

hint_5 = Scene("Help", "hint_5",
"""
'To find the map, one simply needs to look towards the burned heaven of lodge 1097, it will lead the way.'
What's the code?
""")

underground = Scene("Underneath Tower Bridge", "underground",
"""
The door clicks and swings open.
There is a staircase leading down into the collumn.
You're going down. Your heart's pounding.

After 5min of descend you've reached the bottom. A dark round room with a single pillar in the middle.
What you find takes your breath.
So the legend is true?
This is more serious than you expected.

On the pillar in the middle of the room sits a small pyramid with a flat top.
You have a closer look at it and find an engraving on the surface of the flat top.
You slowly understand: The 'map' was never a real map, it was just a symbol. The actual map is this pyramid.
But how does it point the way to the ancient mysteries?
And why does the pyramid have a flat top? The capstone is missing...

You're trying to read the engravings:


         i
         O
        [o]
        The legend will be found at the 33rd degree -> */\*


You have no idea what i O [o] means ...
'33rd degree' ... hmmm.
What could '-> */\*' mean, though?

        Let's think:
        -> = direction = go to
        ** = star = sacred = church
        /\ = top = view = high

You start to understand: The legend will be found at a sacred, high viewpoint in London.

Where do you go?

Type "help" if you don't understand yet.
""")

hint_6 = Scene("Help", "hint_6",
"""
Come on. Think!
What's a famous church or cathedral in the heart on London?
""")

st_pauls = Scene("At St. Paul's Cathedral", "st_pauls",
"""
You've made to St. Paul's Cathedral.
*/\* can only point to the viewing gallery of the dome. It used to be the highest point in London.
You're going up to St. Paul's viewing platform.

You're walking round the viewing gallery wondering if this the right place
as thousands of tourist come here every day,
when something the catches your eye ...
A small symbol on the wall:

                [o]

You slowly realise where you've seen this symbol before.
You take another look at the pyramid in your bag and your assumption confirms itself.
You're having a closer look at the symbol on the wall and notice
that it is actully engraved on some sort of disc build into the dome's wall.
You wonder if it is moveable.
You remember:'The legend will be found at the 33rd degree'

What do you do?

Type "help" if you don't understand yet.
"""
)

hint_7 = Scene("Help", "hint_7",
"""
Ok, this is a hard one.
The disc looks like it's moveable.
... 'The legend will be found at the 33rd degree' ...
33rd degree might mean a rotation of 33 degrees, no?
Wanna try to rotate it?
""")

the_capstone = Scene("The Capstone", "the_capstone",
"""
The disc disappears into the wall and leaves a small round hole.

Your finger touch a cool, small object.
It feels like ... wait ... no, that can't be.

You pull your hand out.
In your hand lies an even smaller pyramid. Made out of solid gold.
Wait: So this is the legend of the ancient mysteries? The wisdom of the forgotten world?
No .. and slowly you start to understand ...
'This must be the missing capstone!'

On the golden capstone you find very delicate engravings:

    i commemorates the Great Fire of London
    O takes one from earth to heaven and reverse

Where do you go?

Type in "help" if you don't understand yet.
""")

hint_8 = Scene("Help", "hint_8",
"""
Let's take another look at the original pyramid:
     i
     O
    [o]
    The legend will be found at the 33rd degree -> */\*

The capstone is not THE legend. It is A legend. A Legend to read the map, to decipher the pyramid.
'i commemorates the Great Fire of London'
What place commemorates the Great Fire of London?
""")

monument = Scene("At the Monument", "monument",
"""
Yes, excellent! The Monument to the Great Fire of London, a Doric column not far from here, commemorates the Great Fire of London.

You have arrived at the The Monument to the Great Fire of London.
There is only one last puzzle to solve.
You have the map and the legend.

             i - solved that: The Monument
             O - 'takes one from earth to heaven and reverse.' hmm ...
            [o] - hmmm ...

'O takes one from earth to heaven and reverse.'
Think more specific:
How do you ascend and descend a building like the Monument?
Hint: It takes a lot of steps...
"""
)

monument_staircase = Scene("The Staircase", "monument_staircase",
"""
Excatly! Now have a look inside the Monument:
There is a spiral staircase inside that takes you up to the top of the collumn.
But take another a look at the map.

             i - The Monument
             O - Spiral Staircase
            [o]

'[o]' must be the symbol for the ancient mysteries.

Let us assemble everything:

             i - The Monument
             O - Spiral Staircase
            [o] - The Ancient Mysteries

Up or down?
""")

final = Scene ("Final - Inside the Monument", "final",
"""
You are now inside at the base of the Monument.
But there is no staircase going down. Only the one going up.

Wait ... there is a small hatch in the floor!
There is an old rusty combination lock on it.
The code is 8 digits!
There is a poem engraved on the back of the lock:

            Sparks from a baker's oven
            Set the blaze with hellish fury
            Timbers dry from sweltering summer
            House after house bursting into flame.


The code must have something to do with the great fire of London!
8 digits ... could be a historic date, no?
What's the code?

Type "help" if you don't know yet.
"""
)

hint_9 = Scene("Help", "hint_9",
"""
When was the Great Fire of London?
""")

the_end = Scene("Final", "the_end",
"""
Do you really want to do this?
The lock clicks and opens.
Well done! You've solved everything!
You can now go down the staircase to unleash the ancient mysteries.
Do you really want to do this?
""")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
Have fun! But don't destroy the world.
You won!
""")

the_end_loser = Scene("The End", "the_end_loser",
"""
Ok, very wise ... maybe it is better not to.
You've made it and won the game anyways!
""")

generic_death = Scene("Death ...", "death", "You died.")

try_again = Scene("Nope, wrong answer!", "try_again",
"""
Come on, you can do better.
""")

#Define the action commands available in each Scene
the_end.add_paths({
    'yes': the_end_winner,
    'no': the_end_loser
})

hint_9.add_paths({
    '02091666': the_end
})

final.add_paths({
    '02091666': the_end
})

monument_staircase.add_paths({
    'down': final
})

monument.add_paths({
    'stairs': monument_staircase,
    'staircase': monument_staircase
})

hint_8.add_paths({
    'The Monument': monument,
    'the monument': monument,
    'monument': monument
})

the_capstone.add_paths({
    'The Monument': monument,
    'the monument': monument,
    'monument': monument,
    'help': hint_8
})

hint_7.add_paths({
    'yes': the_capstone
})

st_pauls.add_paths({
    '33 degrees': the_capstone,
    'move it': the_capstone,
    'spin it': the_capstone,
    'rotate': the_capstone,
    'move': the_capstone,
    'help': hint_7
})

hint_6.add_paths({
    'stpauls': st_pauls,
    'st pauls': st_pauls,
    'StPauls': st_pauls,
    'St. Pauls': st_pauls,
    'st. pauls': st_pauls
})

underground.add_paths({
    'stpauls': st_pauls,
    'st pauls': st_pauls,
    'StPauls': st_pauls,
    'St. Pauls': st_pauls,
    'st. pauls': st_pauls,
    'help': hint_6
})

hint_5.add_paths({
    '1097': underground
})

inside_tower_bridge.add_paths({
    '1097': underground,
    'help': hint_5
})

hint_4.add_paths({
    'yes': inside_tower_bridge
})

tower_bridge.add_paths({
    'help': hint_4,
    'inside': inside_tower_bridge,
    'chambers': inside_tower_bridge,
    'chamber': inside_tower_bridge,
    'collumn': inside_tower_bridge,
    'help': hint_4
})

ceiling.add_paths({
    'tower bridge': tower_bridge,
    'Tower Bridge': tower_bridge,
    'towerbridge': tower_bridge
})

hint_3.add_paths({
    'heaven': ceiling,
    'up': ceiling,
    'ceiling': ceiling
})

lodge_1097.add_paths({
    'heaven': ceiling,
    'up': ceiling,
    'ceiling': ceiling
})

hint_2.add_paths({
    'lodge': lodge_1097,
    'lodge 1097': lodge_1097,
    'lodge no. 1097': lodge_1097
})

phone_call.add_paths({
    'lodge': lodge_1097,
    'lodge 1097': lodge_1097,
    'lodge no. 1097': lodge_1097,
    'help': hint_2
})

parliament.add_paths({
    'yes': phone_call,
    'lodge': lodge_1097,
    'lodge 1097': lodge_1097,
    'help': hint_2
})

hint_1.add_paths({
    'parliament': parliament
})
westminster_bridge.add_paths({
    'parliament': parliament,
    'help': hint_1
})

welcome.add_paths({
    'yes': westminster_bridge
})

# Make some useful variables to be used in the web application
SCENES = {
    welcome.urlname : welcome,
    westminster_bridge.urlname : westminster_bridge,
    parliament.urlname : parliament,
    hint_1.urlname : hint_1,
    phone_call.urlname : phone_call,
    hint_2.urlname : hint_2,
    lodge_1097.urlname : lodge_1097,
    hint_3.urlname : hint_3,
    ceiling.urlname : ceiling,
    tower_bridge.urlname : tower_bridge,
    hint_4.urlname : hint_4,
    inside_tower_bridge.urlname : inside_tower_bridge,
    hint_5.urlname : hint_5,
    underground.urlname : underground,
    hint_6.urlname : hint_6,
    st_pauls.urlname : st_pauls,
    hint_7.urlname : hint_7,
    the_capstone.urlname : the_capstone,
    hint_8.urlname : hint_8,
    monument.urlname : monument,
    monument_staircase.urlname : monument_staircase,
    final.urlname : final,
    hint_9.urlname : hint_9,
    the_end.urlname : the_end,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    generic_death.urlname : generic_death,
    try_again.urlname : try_again
}
START = welcome
