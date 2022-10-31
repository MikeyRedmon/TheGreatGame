def introduction():
    answer = input("Welcome to The Greatest Game! Do you want to play?").lower().strip()
    if answer == "yes":
        play_game()
    else:
        print("Sorry to hear, You're missing out.")
    

def play_game():


introduction()