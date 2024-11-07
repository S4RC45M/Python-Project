import random

retry = True

gendNum = random.randrange(2, 11)

numTries = 0

while retry == True:
    print("Guess a number between 1 and 10.")
    if numTries == 3:
        print("Would you like a hint? Y/N")
        hint = input()
        if hint == str("Y"):
            if gendNum < 4:
                print("The number I'm thinking of is less than 4.")
            elif 4 >= gendNum < 7:
                print("The number I'm thinking of is bewtween 3 and 7.")
            elif gendNum > 6:
                print("The number I'm thinking of is larger than 6.")
            numTries = numTries - 3
        elif hint == str("N"):
            numTries = numTries - 3
            continue
    numGuess = input()
    if str(numGuess) == str(gendNum):
        print("That's correct!")
        print("Would you like to go again? Y/N")
        retryInput = input()
        if retryInput == str("Y"):
            retry = True
        elif retryInput == str("N"):
            retry = False
            print("Thanks for playing!")
            break
    else:
        print("Sorry that is incorrect.")
        print("Would you like to retry? Y/N")
        retryInput = input()
        if retryInput == str("Y"):
            retry = True
            numTries = numTries + 1
        elif retryInput == str("N"):
            retry = False
            print("Thanks for playing!")
            break
