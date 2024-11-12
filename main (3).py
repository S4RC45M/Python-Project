import random

retry = True

gendNum = random.randrange(2, 11)

numTries = 0

while retry:
    print("Guess a number between 1 and 10.")
    if numTries == 3:
        print("Would you like a hint? Y/N")
        hint = input()
        if hint == "Y":
            if gendNum < 4:
                print("The number I'm thinking of is less than 4.")
            elif 4 >= gendNum < 7:
                print("The number I'm thinking of is bewtween 3 and 7.")
            elif gendNum > 6:
                print("The number I'm thinking of is larger than 6.")
            numTries = 0
        else:
            numTries = 0
            continue
    numGuess = input()
    if str(numGuess) == str(gendNum):
        print("That's correct!")
    else:
        print("Sorry that is incorrect.")
    print("Would you like to go again? Y/N")
    retryInput = input().upper()
    if retryInput == "Y":
        retry = True
    elif retryInput == "N":
        retry = False
        print("Thanks for playing!")
        break
    else:
        print("Thanks for playing!")
        break
