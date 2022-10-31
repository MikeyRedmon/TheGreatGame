def introduction():
    answer = input("Welcome to The Greatest Game! Do you want to play?").lower().strip()
    if answer == "yes":
        play_game()
    else:
        print("Sorry to hear, You're missing out.")
        introduction()
        

def play_game():
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

def begger_room():

introduction()