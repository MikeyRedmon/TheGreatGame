from xml.etree import ElementInclude


def introduction():
    '''Ran when program starts. Asks player if they want to play'''
    answer = input("Welcome to The Greatest Game! Do you want to play?\n Mild arachnophobia warning, violence warning.").lower().strip()
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
    else:
        print("Please enter a valid option")
        begger_room()


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
        transition()
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
    elif answer == "talk":
        print("The goblins seem hesitant at first. But after you raise your hands and explain yourself, they seem perfectly fine with letting you pass.")
        transition()


def transition():
    '''Function that bridges between phase one and two'''
    print("As you walk through the dungeon you begin to notice natural light beginning to snake its way through the cracks in the ceiling.\nThe air smells fresher. Walking into a slightly more open space you spot a small well with fresh water.\n After a few moments rest you continue.")
    answer = input("The stone passageways are now more mossy. Covered in a slight damp as you enter a large ruined room.\nThe ceiling is half caved in, but you can still see various halls. \n But what catches your eye is an iron gate on the floor above you.\n Where do you go?").lower().strip()
    if answer == "explore":
        print("You take some time to explore, walking down a hallway you slip as you turn a corner. The last thing you remember is falling. GAME OVER.")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    elif answer == "gate":
        print("Climbing up some stones to the second floor, you spot a bit of sky through a few pieces of rubble. You're almost there. Just have this gate to get through...")
        the_gate()
    else:
        print("Please enter a valid choice")
        transition()


def the_gate():
    '''Function that runs the gate encounter'''
    answer = input("The old, rust and moss covered Iron gate.\n What do you do?").lower().strip()
    if answer == "climb the gate":
        print("You rub your hands together and try to climb up the gate.\n A few rungs up you lose your grip and fall. GAME OVER")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    elif answer == 'investigate':
        print("Next to the gate in an alcove is an old, rust and moss covered wench.")
        wench()
    else:
        print("Please input a valid choice")
        the_gate()


def wench():
    '''Function for wench encounter'''
    answer = input("You see the wench system, its covered in moss and rust. It looks to be the easiest way out however.").lower().strip()
    if answer == "use sword":
        print("You use the sword as leverage and after putting some strain into it you hear a sickening snap noise.\n You feel something hot explode down your chest. You look down, the broken end of your blade stuck in your chest.\n GAME OVER")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    elif answer == "explore":
        print("You look around, spotting several hallways on this floor.\n However, only one of them seems to be accessable.\n You head toward the hall.")
        mossy_hallway()
    else:
        print("please input a valid choice")
        wench()


def mossy_hallway():
    '''The function that runs the last major choice scenario'''
    answer = input("You see two doors down the hallway. Which one do you go down?").lower().strip()
    if answer == "first door":
        print("Entering the first door you look around for anything that might be useful.\n Just as you feel a presence behind you, you feel an impact on the back of your head.\n GAME OVER.")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    elif answer == "second door":
        choice = input("You see a pair of giant spiders, covered in thick moss.\n Both of them seem unawares of you as they scuttle about. Fixing a web made from moss. In the corner of the room you see a small oil can.\n What do you do?").lower().strip()
        if choice == "sneak":
            print("you attempt to sneak around the spiders. As you get close to the oil can you feel your leg touch a mossy web.\n The two spiders immedately jump you.\n GAME OVER.")
            again = input("Do you want to try again?").lower().strip()
            if again == "yes":
                introduction()
            else:
                print("Tough luck! We hope you enjoyed The Greatest Game!")
        elif choice == "attack":
            print("You swing your weapon. While the spiders are large, they're surpsingly brittle.\nYou take the oil can.")
            end()
    else:
        print("Please input a valid choice")
        mossy_hallway()


def end():
    '''Function that runs at the end of the game cycle.'''
    print("Walking back to the wench system, you apply whats left in the oil can liberally.\n Testing the wench after a few minutes, it begins to give. The gate raises.\nAt the end of the hallway you see a spiral staircase.\nYou climb out into the world, emerging in a ruined building. END")
    print("Thank you for playing! I really appreciate it and hope you had as much fun as I did writing it!")


introduction()
