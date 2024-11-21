import CometDict
from Question import Question
import random as r
import time

def compare(n1, n2):
    if n1.answer < n2.answer:
        return n2.name
    elif n1.answer > n2.answer:
        return n1.name

data = CometDict.spaceobjects
ongoing = True
tries = 0 
spaceobjlen = len(data) 

print("Compare the distance of two objects in space compared to how close they are to the sun!\n")
while ongoing:
        randnum1 = r.randint(0,(spaceobjlen-1))
        randnum2 = r.randint(0,(spaceobjlen-1))
        space1 = Question(data[randnum1]["name"], data[randnum1]["orbityears"])
        space2 = Question(data[randnum2]["name"], data[randnum2]["orbityears"])
        if space1.name == space2.name:
            pass
        else:             
            useranswer = input(f"which object is further away from the sun, {space1.name} or {space2.name}?\n")
            actualanswer = compare(space1,space2)
            if (useranswer.capitalize() == actualanswer):
                    print("correct")
            else:
                    print(f"incorrect, the answer was {actualanswer}")
