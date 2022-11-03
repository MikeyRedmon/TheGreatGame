from xml.etree import ElementInclude


def introduction():
    '''Ran when program starts. Asks player if they want to play'''
    answer = input("Welcome to The Greatest Game! Do you want to play?").lower().strip()
    if answer == "yes":
        play_game()
    else:
        print("Sorry to hear, You're missing out.")
        introduction()
       

def play_game():
    '''Function that starts the game and offers the player the first of their choices'''
    answer = input("You wake up in a cold, dark cell.\n You don't remember how you ended up here.\n But you know you must get out.\n The cell bars are broken and rusted, like something tore them apart from the inside out,\n You'd rather not meet the creature who did this.\n So you leave. You come to a hallway with an intersection. One goes right, one goes left and one straight.\n Which way do you go?").lower().strip()
    if answer == "left":
        print("Down the hall to the left you come to a room,\n inside you see a hand and a half sword\n its simple, but sharp and well weighted.\n Beside it you see a pouch of gold. You take the items\n knowing you'll need them.")
        begger_room()
    elif answer == "center":
        print("The hallway is long and barren, no torches light the way as you spot a wooden door. Its ajar. You enter.")
        begger_room()
    elif answer == "right":
        print("The hallway smells of death, with a coppery tinge hanging in the air. You clench your teeth and step forward.\n You hear a chunk and look down. You've stepped on a pressure plate.\n The last thing you hear is the grind of metal on stone. GAME OVER")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    else:
        print("Please input a direction")
        play_game()


def begger_room():
    '''Function that starts the begger room sequence.'''
    answer = input("Entering the room you you see more old worn stone. The room has three things of interest.\n Sitting off to the side and covered in rags is an individual down on their luck.\n They glance up at you but don't maintain eye contact.\n Their are two doors, one heading left and one heading right.").lower().strip()
    if answer == "attack the begger":
        print("The begger looks up as you charge toward them. You swing your weapon.\n An aura surrounds the begger as your weapon freezes mid air. 'Not the Smartest decision you've made.'\n They speak with a disapointment hanging in their tone.\n The world blurs and you feel yourself zip across the room... GAME OVER")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    elif answer == "give the begger money":
        print("You hand the begger some money. They look up at you with tired yet bright eyes.\n 'Thank you. Here, no good deed should go unrewarded.'\n They hand you a leather chestpiece.")
    elif answer == "left":
        print("Heading left you find yourself in a large room.\nThe rooms right side is collapsed in. A goblin civilization seems to have made this place apart of their home.")
        goblin_encounter()
    elif answer == "right":
        print("Heading right you find yourself in a medium sized room.\nThe room contains a very spartan room. A large bullman, a Minotaur stands at a table with a large two handed axe on the table.\n Hes sharpening the blades.")
        minotaur_encounter()


def minotaur_encounter():
    '''Function that starts the minotaur encounter'''
    answer = input("Walking down a short stoney hallway the player walks into a small room, it has a very spartan look.\n A bed and very little else takes up a bit of space in the corner. Though the massive Minotaur sitting at a desk with a heavy axe with their back to the door might be bigger.\n What do you do?").lower().strip()
    if answer == "fight" or "talk":
        print("The Minotaur turns to you, their eyes immediately flairing in anger as they pick up the axe with one hand and swing it toward you.\n Caught unawares you take the full brunt of it to the side. The world zips and you fall unconcious. GAME OVER")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    elif answer == "sneak":
        print("You sneak past the Minotaur, knowing to keep your head slow and your movements slow but commited.\nYou make it past the room and out the other side")
        next_Level()
    else:
        print("Please enter a viable choice")
        minotaur_encounter()


def goblin_encounter():
    '''Function that starts the goblin encounter'''
    answer = input("The hallway has more broken stone and cracked wall than before. Walking into what might have been a room at some point, half the wall happens to be torn down.\nThe dirt wall has been transformed into a small selection of in and out tunnels.\n You can see some goblins milling about and talking. What do you do?").lower().strip()
    if answer == "attack" or "fight":
        print("You rush in, swinging your weapon you take the first small group off guard. But then you notice the many, many eyes glaring back at you from the wall...\n It takes time, but you find yourself exhausted. Unable to fight any longer. GAME OVER.")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    if answer == "talk":
        print("The goblins seem hesitant at first. But after you raise your hands and explain yourself, they seem perfectly fine with letting you pass.")
        transition()

def transition():
    '''Function that bridges between phase one and two'''
    print("As you walk through the dungeon you begin to notice natural light begining to snake its way through the cracks in the ceiling.\nThe air smells fresher. Walking into a slightly more open space you spot a small well with fresh water.\n After a few moments rest you continue.")
    


introduction()
