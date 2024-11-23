import random
import CometDict
from Question import Question
import random as r

def compare(n1, n2):
    if n1.answer < n2.answer:
        return n2.name
    elif n1.answer > n2.answer:
        return n1.name

data = CometDict.spaceobjects
ongoing = True
spaceobjlen = len(data)

def distanceGame():
    print("Guess how far two objects are to the Sun!\n")
    while ongoing:
        randnum1 = r.randint(0, (spaceobjlen - 1))
        randnum2 = r.randint(0, (spaceobjlen - 1))
        space1 = Question(data[randnum1]["name"], data[randnum1]["orbityears"])
        space2 = Question(data[randnum2]["name"], data[randnum2]["orbityears"])
        if space1.name == space2.name:
            pass
        else:
            useranswer = input(f"which object is further away from the sun, {space1.name} or {space2.name}?\n")
            actualanswer = compare(space1, space2)
            if useranswer == actualanswer:
                print("correct")
            else:
                print("incorrect")

def randNumGame():
    gendNum = random.randrange(2, 11)

    numTries = 0

    while True:
        print("I have generated a new number.")
        print("Guess a number between 1 and 10.")
        #This is to give the player a hint after 3 tries
        if numTries == 3:
            print("Would you like a hint? Y/N")
            hint = input()
            hint = hint.upper()
            if hint == "Y":
                if gendNum < 4:
                    print("The number I'm thinking of is less than 4.")
                elif 4 >= gendNum < 7:
                    print("The number I'm thinking of is between 3 and 7.")
                elif gendNum > 6:
                    print("The number I'm thinking of is larger than 6.")
                numTries = 0
            elif hint == "N":
                numTries = 0
                continue
            else:
                print("Please enter a valid response.")
        #Players guess what number has been generated
        numGuess = input()
        if numGuess == gendNum:
            print("That's correct!")
            print("Would you like to go again? Y/N")
            retryInput = input()
            retryInput = retryInput.upper()
            if retryInput == "Y":
                continue
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
                numTries = numTries + 1
            elif retryInput == "N":
                print("Thanks for playing!")
                break
            else:
                print("Please enter a valid response.")


def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")

    # Ask if the player is ready to play
    ready = input("Are you ready to play? ")
    if ready != 'yes':
        print("Come back when you're ready!")
        return

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()

        # Allow the user to quit the game
        if user_choice == 'q':
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Generate a random choice for the computer
        computer_choice = random.choice(choices)
        print(f"The computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

        print()  # Print a blank line for spacing


#This is the initial menu for all the games
while True:
    print("Want to Play a Game?")
    print("1. Random Number Game")
    print("2. Rock, Paper, Scissors")
    print("3. Distance Game")
    print("4. Exit")
    choice = input()
    choice = choice.upper()
    if choice == "1":
        randNumGame()
    elif choice == "2":
        rock_paper_scissors()
    elif choice == "3":
        distanceGame()
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Please enter a valid response.")
