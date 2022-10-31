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
    answer = input(f"You wake up in a cold, dark cell.\n You don't remember how you ended up here.\n But you know you must get out.\n The cell bars are broken and rusted, like something tore them apart from the inside out,\n You'd rather not meet the creature who did this.\n So you leave. You come to a hallway with an intersection. One goes right, one goes left and one straight.\n Which way do you go?").lower().strip()
    if answer == "left":
        print(f"Down the hall to the left you come to a room,\n inside you see a hand and a half sword\n its simple, but sharp and well weighted.\n Beside it you see a pouch of gold. You take the items\n knowing you'll need them.")
        begger_room()
    elif answer == "center":
        print(f"The hallway is long and barren, no torches light the way as you spot a wooden door. Its ajar. You enter.")
        begger_room()
    elif answer == "right":
        print(f"The hallway smells of death, with a coppery tinge hanging in the air. You clench your teeth and step forward.\n You hear a chunk and look down. You've stepped on a pressure plate.\n The last thing you hear is the grind of metal on stone. GAME OVER")
        again = input(f"Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    else: 
        print("Please input a direction")


def begger_room():
    '''Function that starts the begger room sequence.'''
    answer = input(f"Entering the room you you see more old worn stone. The room has three things of interest.\n Sitting off to the side and covered in rags is an individual down on their luck.\n They glance up at you but don't maintain eye contact.\n Their are two doors, one heading left and one heading right.").lower().strip()
    if answer == "attack the begger":
        print(f"The begger looks up as you charge toward them. You swing your weapon.\n An aura surrounds the begger as your weapon freezes mid air. 'Not the Smartest decision you've made.'\n They speak with a disapointment hanging in their tone.\n The world blurs and you feel yourself zip across the room... GAME OVER")
        again = input("Do you want to try again?").lower().strip()
        if again == "yes":
            introduction()
        else:
            print("Tough luck! We hope you enjoyed The Greatest Game!")
    elif answer == "give the begger money":
        print(f"You hand the begger some money. They look up at you with tired yet bright eyes.\n 'Thank you. Here, no good deed should go unrewarded.'\n They hand you a leather chestpiece.")
    

introduction()
