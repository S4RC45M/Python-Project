import random

def gameChoices():
    print("What game would you like to play?")
    print("1. Random Number Game")
    print("2. Exit")
    choice_games = input()
    if choice_games == "1":
        randNumGame()
    elif choice_games == "2":
        print("Exiting...")
    else:
        print("Please enter 1 or 2")

def randNumGame():
    gendNum = random.randrange(1, 11)

    numTries = 0

    retry = True

    while retry:
        print("I have generated a new number.")
        print("Guess a number between 1 and 10.")
        #This gives the player a hint after 3 tries
        if numTries == 3:
            print("Would you like a hint? Y/N")
            hint = input()
            hint = hint.upper()
            if hint == "Y":
                if gendNum <= 4:
                    print("The number I'm thinking of is less than 4.")
                elif 4 >= gendNum < 7:
                    print("The number I'm thinking of is between 3 and 7.")
                elif gendNum >= 6:
                    print("The number I'm thinking of is larger than 6.")
                numTries = 0
            elif hint == "N":
                numTries = 0
                continue
            else:
                print("Please enter a valid response.")
        #Get input from player and determine if it is correct or not
        numGuess = input()
        if numGuess == gendNum:
            print("That's correct!")
            print("Would you like to go again? Y/N")
            retryInput = input()
            retry = retry.upper()
            if retryInput == "Y":
                retry = True
            elif retryInput == "N":
                print("Thanks for playing!")
                break
            else:
                print("Please enter a valid number.")
        else:
            print("Sorry that is incorrect.")
            print("Would you like to retry? Y/N")
            retryInput = input()
            retryInput = retryInput.upper()
            if retryInput == "Y":
                retry = True
                numTries = numTries + 1
            elif retryInput == "N":
                print("Thanks for playing!")
                break
            else:
                print("Please enter a valid response.")
#This is the menu system for all the games
while True:
    print("Want to Play a Game? Y/N")
    choice = input()
    choice = choice.upper()
    if choice == "Y":
        gameChoices()
    elif choice == "N":
        print("Okay, see you later!")
        break
    else:
        print("Please enter a valid response.")
