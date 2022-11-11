# Import Random for the random elements of the game
import random
# Import Textwrap to wrap long text for better visuals
import textwrap
# Import Colorama for a better, more visually appealing experiance.
from colorama import Fore, Back, Style


# Colour Tags

t_color = Fore.LIGHTRED_EX      # Terminal Colour
i_color = Fore.LIGHTCYAN_EX     # Imput Colour
e_color = Back.RED              # Error Colour
s_color = Fore.LIGHTMAGENTA_EX  # Secret Colour
d_color = Fore.GREEN            # Death Text
reset_all = Style.RESET_ALL     # Reset to normal

# Arry of weapons for the random weapon choice

weapons = [
    "Arming Sword", "Dagger", "Longsword",
    "Flanged Mace", "Morning Star", "Halbard", "Glaive"
    ]

# Generator that pushes a single interger to the num value


def gold():
    '''Generates random number of gold pieces'''
    for num in range(2, 50):
        num = random.randint(2, 50)
        return num


# The Hint list returns a hint for the player.


hints = [
    "Be Kind",
    "Be sure to read all the text",
    "Give some to gain a lot",
    "Sit and stay a while...",
    "You're looking for a way out.",
    "Exploring is always an option.",
    "Always try to go up."
    ]


def welcome():
    '''
    Runs when app starts
    introduces player to what the game is
    '''
    print(Fore.BLUE + '''
                    |>>>                        |>>>
                    |                           |
                _  _|_  _                   _  _|_  _
               | |_| |_| |                 | |_| |_| |
               \  .      /                 \ .    .  /
                \    ,  /                   \    .  /
                 | .   |_   _   _   _   _   _| ,   |
                 |    .| |_| |_| |_| |_| |_| |  .  |
                 | ,   | .    .     .      . |    .|
                 |   . |  .     . .   .  ,   |.    |
     ___----_____| .   |.   ,  _______   .   |   , |---~_____
_---~            |     |  .   /+++++++\    . | .   |         ~---_
                 |.    | .    |+++++++| .    |   . |              ~-_
              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
 -~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~
        ''')
    print(
        t_color +
        textwrap.fill(
            "Welcome to The Greatest Game!"
            " This is a text based adventure game in which"
            " you, as the player must figure out whats going on"
            " Their are several secrets and multiple options"
            " I hope you enjoy the game! I had fun making it."
            )
        )
    introduction()


def introduction():
    '''Asks player if they want to play'''
    print(reset_all)
    answer = input(
        i_color + textwrap.fill(
            "Mild arachnophobia warning, violence warning."
            " Do you want to play?"
        )
    ).lower().strip()
    print(reset_all)
    if answer == "yes":
        play_game()
    else:
        print(t_color + "Sorry to hear, You're missing out.")
        print(reset_all)


def play_game():
    '''
    Function that starts the game and offers
    the player the first of their choices
    '''
    print(reset_all)
    print(
        t_color + textwrap.fill(
            "You wake up in a cold, dark cell."
            "You don't remember how you ended up here."
            "But you know you must get out."
            "The cell bars are broken and rusted,"
            "like something tore them apart from the inside out"
            "You'd rather not meet the creature who did this So you leave."
        )
    )
    print(reset_all)
    answer = input(
        i_color +
        "You come to an intersection."
        "One goes Left, One goes right and one continues straight."
        "Where do you go?"
        ).lower().strip()
    print(reset_all)
    if answer == "left":
        print(
            s_color +
            "Down the hall to the left you come to a room"
            f" inside you see a {random.choice(weapons)}"
            " its simple, but maintained and well weighted."
            f"Beside it you see a pouch of {gold()} gold."
            " You take the items knowing you'll need them."
        )
        begger_room()
        print(reset_all)
    elif answer == "straight":
        print(
            t_color +
            textwrap.fill(
                "The hallway is long and barren"
                "no torches light the way as you spot a wooden door."
                "Its ajar. You enter."
                )
            )
        begger_room()
        print(reset_all)
    elif answer == "right":
        print(
            d_color +
            textwrap.fill(
                "The hallway smells of death"
                "with a coppery tinge hanging in the air."
                "You clench your teeth and step forward."
                "You hear a chunk and look down."
                "You've stepped on a pressure plate."
                "The last thing you hear is the grind of metal on stone."
                "GAME OVER"
                )
            )
        print(reset_all)
        again = input(i_color + "Do you want to try again?").lower().strip()
        if again == "yes":
            play_game()
        else:
            print(t_color + "Tough luck We hope you enjoyed The Greatest Game")
            print(reset_all)
    elif answer == "sleep":
        print(
            s_color +
            "You decide to just go back to bed."
            "Today isn't the day for this")
        print(reset_all)
        introduction()
    elif answer == "hint":
        print(t_color + f"{random.choice(hints)}")
        play_game()
    else:
        print(e_color + "Please input a direction")
        print(reset_all)
        play_game()


def begger_room():
    '''Function that starts the begger room sequence.'''
    print(reset_all)
    answer = input(
        i_color + textwrap.fill(
            "Entering the room you you see more old worn stone."
            "The room has three things of interest."
            "Sitting off to the side and covered in rags"
            "is an individual down on their luck."
            "They glance up at you but don't maintain eye contact."
            "Their are two doors, one heading left and one heading right."
        )
    ).lower().strip()
    print(reset_all)
    if answer == "attack the begger":
        print(
            d_color + textwrap.fill(
                "The begger looks up as you charge toward them."
                "You swing your weapon."
                "An aura surrounds the begger as your weapon freezes mid air."
                "'Not the Smartest decision you've made.'"
                "They speak with a disapointment hanging in their tone."
                "The world blurs and you feel yourself zip across the room..."
                "GAME OVER"
                )
            )
        print(reset_all)
        again = input(t_color + "Do you want to try again?").lower().strip()
        print(reset_all)
        if again == "yes":
            play_game()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
            print(reset_all)
    elif answer == "give the begger money":
        print(
            s_color +
            textwrap.fill(
                "You hand the begger some money."
                "They look up at you with tired yet bright eyes."
                "'Thank you. Here, no good deed should go unrewarded.'"
                "They hand you a leather chestpiece."
                )
            )
        print(reset_all)
        begger_room()
    elif answer == "left":
        print(
            t_color +
            "Heading left you find yourself in a large room."
            "The rooms right side is collapsed in."
            "A goblin civilization seems to have"
            "made this place apart of their home."
            )
        print(reset_all)
        goblin_encounter()
    elif answer == "right":
        print(
            t_color +
            textwrap.fill(
                "Heading right you find yourself in a medium sized room."
                "The room contains very litte. Spartan."
                "A large bullman, a Minotaur stands at a table"
                "with a large two handed axe on the table."
                "Hes sharpening the blades."
                )
            )
        minotaur_encounter()
    elif answer == "sit with begger":
        print(
            s_color +
            textwrap.fill(
                "You sit down next to the begger, unsure of what to say."
                "You think you know them. They turn their head to you and nod."
                "'I see you've woken up, my friend. Good.'"
                "The world flashes before you. You remember... Everything."
                )
            )
        print(reset_all)
        secret_ending_one()
    elif answer == "hint":
        
        begger_room()
    else:
        print(e_color + "Please enter a valid option")
        print(reset_all)
        begger_room()


def minotaur_encounter():
    '''Function that starts the minotaur encounter'''
    print(reset_all)
    answer = input(
        "Walking down a short stone hallway the player walks into a small room"
        "it has a very spartan look."
        "A bed and very little else takes up a bit of space in the corner."
        "Though the massive Minotaur sitting at a desk with a heavy axe"
        "and their back to the door might be bigger. What do you do?"
        ).lower().strip()
    if answer == "fight":
        print(
            d_color +
            textwrap.fill(
                "The Minotaur turns to you, their eyes immediately flairing"
                "in anger as they pick up the axe with"
                "one hand and swing it toward you."
                "Caught unawares you take the full brunt of it to the side."
                "The world zips and you fall unconcious."
                "GAME OVER"
                )
            )
        print(reset_all)
        again = input(i_color + "Do you want to try again?").lower().strip()
        if again == "yes":
            play_game()
            print(reset_all)
        else:
            print(t_color + "Tough luck We hope you enjoyed The Greatest Game")
            print(reset_all)
    elif answer == "sneak":
        print(
            t_color +
            "You sneak past the Minotaur"
            "knowing to keep your head low"
            "and your movements slow but commited."
            "You make it past the room and out the other side"
            )
        print(reset_all)
        transition()
    else:
        print(e_color + "Please enter a viable choice")
        print(reset_all)
        minotaur_encounter()


def goblin_encounter():
    '''Function that starts the goblin encounter'''
    print(reset_all)
    answer = input(
        i_color +
        textwrap.fill(
            "The hallway has more broken stone and cracked wall than before."
            "Walking into what might have been a room at some point"
            "half the wall happens to be torn down."
            "The dirt wall has been transformed"
            "into a small selection of in and out tunnels."
            "You can see some goblins milling about and talking."
            "What do you do?"
            )
        ).lower().strip()
    print(reset_all)
    if answer == "attack":
        print(
            d_color +
            textwrap.fill(
                "You rush in, swinging your weapon"
                "you take the first small group off guard."
                "But then you notice the many, many eyes glaring"
                "back at you from the wall..."
                "...It takes time, but you find yourself exhausted."
                "Unable to fight any longer."
                "GAME OVER."
                )
            )
        print(reset_all)
        again = input(i_color + "Do you want to try again?").lower().strip()
        print(reset_all)
        if again == "yes":
            play_game()
        else:
            print(t_color + "Tough luck We hope you enjoyed The Greatest Game")
            print(reset_all)
    elif answer == "talk":
        print(
            t_color +
            "The goblins seem hesitant at first."
            "But after you raise your hands and explain yourself,"
            "they seem perfectly fine with letting you pass."
            )
        print(reset_all)
        transition()
    elif answer == "hint":
        print(t_color + f"{random.choice(hints)}")
        minotaur_encounter()
    else:
        print(t_color + "Please enter a viable choice")
        print(reset_all)
        goblin_encounter()


def transition():
    '''Function that bridges between phase one and two'''
    print(reset_all)
    print(
        t_color +
        textwrap.fill(
            "As you walk through the dungeon you begin to notice natural light"
            "beginning to snake its way through the cracks in the ceiling."
            "The air smells fresher. Walking into a slightly more open space"
            "you spot a small well with fresh water."
            "You drink from the well, feeling more normal"
            "After a few moments rest you continue."
            )
        )
    print(reset_all)
    answer = input(
        i_color +
        textwrap.fill(
            "The stone passageways are now more mossy."
            "Covered in a slight damp as you enter a large ruined room."
            "The ceiling is half caved in"
            "but you can still see various halls."
            "But what catches your eye is an iron gate"
            "on the floor above you. Where do you go?"
            )
        ).lower().strip()
    print(reset_all)
    if answer == "explore":
        print(
            d_color +
            "You take some time to explore"
            "walking down a hallway you slip as you turn a corner."
            "The last thing you remember is falling."
            "GAME OVER."
            )
        print(reset_all)
        again = input("Do you want to try again?").lower().strip()
        print(reset_all)
        if again == "yes":
            play_game()
        else:
            print(t_color + "Tough luck We hope you enjoyed The Greatest Game")
            print(reset_all)
    elif answer == "up":
        print(
            t_color +
            "Climbing up some stones to the second floor"
            "you spot a bit of sky through a few pieces of rubble."
            "You're almost there. Just have this gate to get through..."
            )
        print(reset_all)
        the_gate()
    elif answer == "climb down":
        print(
            t_color +
            textwrap.fill(
                "You spot a small pile of rubble that looks like"
                "you could knock over to make decending into the pit easy."
                "Curiousity gets the better of you, you knock it over"
                "and heading down into the depths you quickly discover"
                "a large guilded room. On a plaque you read a name"
                "A name that you know. You're family name"
                )
            )
        print(reset_all)
        secret_ending_two()
    elif answer == "hint":
        print(t_color + f"{random.choice(hints)}")
        transition()
    else:
        print(e_color + "Please enter a valid choice")
        print(reset_all)
        transition()


def the_gate():
    '''Function that runs the gate encounter'''
    print(reset_all)
    answer = input(
        i_color +
        "The old, rust and moss covered Iron gate. What do you do?"
        ).lower().strip()
    print(reset_all)
    if answer == "climb the gate":
        print(
            d_color +
            "You rub your hands together and try to climb up the gate."
            "A few rungs up you lose your grip and fall."
            "GAME OVER"
            )
        print(reset_all)
        again = input(i_color + "Do you want to try again?").lower().strip()
        print(reset_all)
        if again == "yes":
            play_game()
        else:
            print(t_color + "Tough luck We hope you enjoyed The Greatest Game")
            print(reset_all)
    elif answer == 'investigate':
        print(
            t_color +
            "Next to the gate in an alcove is an old"
            "rust and moss covered wench.")
        print(reset_all)
        wench()
    elif answer == "hint":
        print(t_color + f"{random.choice(hints)}")
        the_gate()
    else:
        print(e_color + "Please input a valid choice")
        print(reset_all)
        the_gate()


def wench():
    '''Function for wench encounter'''
    print(reset_all)
    answer = input(
        i_color +
        "You see the wench system, its covered in moss and rust."
        "It looks to be the easiest way out however."
        ).lower().strip()
    print(reset_all)
    if answer == "use sword":
        print(
            d_color +
            textwrap.fill(
                "You use the sword as leverage and after putting"
                "some strain into it you hear a sickening snap noise."
                "You feel something hot explode down your chest."
                "You look down the broken end of your blade in your chest."
                "GAME OVER"
                )
            )
        print(reset_all)
        again = input(i_color + "Do you want to try again?").lower().strip()
        print(reset_all)
        if again == "yes":
            play_game()
        else:
            print(t_color + "Tough luck We hope you enjoyed The Greatest Game")
            print(reset_all)
    elif answer == "explore":
        print(
            t_color +
            "You look around, spotting several hallways on this floor."
            "However, only one of them seems to be accessable."
            "You head toward the hall."
            )
        print(reset_all)
        mossy_hallway()
    elif answer == "hint":
        print(t_color + f"{random.choice(hints)}")
        wench()
    else:
        print(e_color + "please input a valid choice")
        print(reset_all)
        wench()


def mossy_hallway():
    '''The function that runs the last major choice scenario'''
    print(reset_all)
    answer = input(
        i_color +
        "You see two doors down the hallway."
        "Which one do you go down?"
        ).lower().strip()
    print(reset_all)
    if answer == "first door":
        print(
            t_color +
            textwrap.fill(
                "Entering the first door you look around"
                "for anything that might be useful."
                "Just as you feel a presence behind you,"
                "you feel an impact on the back of your head."
                "GAME OVER."
                )
            )
        print(reset_all)
        again = input(i_color + "Do you want to try again?").lower().strip()
        print(reset_all)
        if again == "yes":
            play_game()
        else:
            print(t_color + "Tough luck We hope you enjoyed The Greatest Game")
            print(reset_all)
    elif answer == "second door":
        choice = input(
            i_color +
            textwrap.fill(
                "You see a pair of giant spiders, covered in thick moss."
                "Both of them seem unawares of you as they scuttle about."
                "Fixing a web made from moss."
                "In the corner of the room you see a small oil can."
                "What do you do?"
                )
            ).lower().strip()
        print(reset_all)
        if choice == "sneak":
            print(
                t_color +
                textwrap.fill(
                    "You attempt to sneak around the spiders."
                    "As you get close to the oil"
                    "can you feel your leg touch a mossy web."
                    "The two spiders immedately jump you."
                    "GAME OVER."
                    )
                )
            again = input(
                i_color + "Do you want to try again?"
                ).lower().strip()
            print(reset_all)
            if again == "yes":
                play_game()
            else:
                print(
                    t_color +
                    "Tough luck We hope you enjoyed The Greatest Game"
                    )
                print(reset_all)
        elif choice == "attack":
            print(
                t_color +
                "You swing your weapon."
                "While the spiders are large, they're surprisingly brittle."
                "You take the oil can."
                )
            print(reset_all)
            end()
    elif answer == "hint":
        print(t_color + f"{random.choice(hints)}")
        mossy_hallway()
    else:
        print(e_color + "Please input a valid choice")
        print(reset_all)
        mossy_hallway()


def secret_ending_one():
    '''The first secret ending'''
    print(reset_all)
    print(
        t_color +
        textwrap.fill(
            "You see yourself, carrying a bastard sword over your shoulders,"
            "unsure of what you're about to fight."
            "But you know you must not lose"
            "That was the kicker, however. You didn't lose, but the creature"
            "in question infected you."
            "You became a creature of the moon, a Lycanthrope."
            "And the reason you're here is to hide."
            "The Begger is a powerful wizard trying to help you."
            "They're an old friend of your fathers, or something"
            "You dont remember everything, but you know what you"
            "Must do..."
            )
        )
    print(reset_all)
    end()


def secret_ending_two():
    '''The second secret ending'''
    print(reset_all)
    print(
        t_color +
        textwrap.fill(
            "In the room you see several knightly statues,"
            "surrounding a singular stone obelisk."
            "You see names you recognise. Friends, Family, Comrades."
            "This place is a tomb. One that houses the best of your family"
            "One that you're sure means something..."
            "At the foot of the obelisk is a message"
            "'If you're reading this, know you're loved. We'll be waiting'"
            )
        )
    print(reset_all)
    end()


def end():
    '''Function that runs at the end of the game cycle.'''
    print(reset_all)
    print(
        t_color +
        textwrap.fill(
            "Walking back to the wench system,"
            "you apply whats left in the oil can liberally."
            "Testing the wench after a few minutes,"
            "it begins to give. The gate raises."
            "At the end of the hallway you see a spiral staircase."
            "You climb out into the world, emerging in a ruined building."
            "The world is bright and alive, birds chirp and the"
            "breeze on your skin is all you need to know you're"
            "Okay"
            "END"))
    print(
        t_color +
        textwrap.fill(
            "Thank you for playing!"
            "I really appreciate it and hope you"
            "had as much fun as I did writing"
            "and programming it!"
            "There are two secret endings along"
            "with a couple secret encounters. Let me know if you find them."
            )
        )


welcome()
