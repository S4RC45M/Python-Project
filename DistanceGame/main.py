import CometDict
import random as r
data = CometDict.spaceobjects
ongoing = True
spaceobjlen = len(data)
# randnum1 = r.randint(0,(spaceobjlen-1))
# randnum2 = r.randint(0,(spaceobjlen-1))
# print(data, spaceobjlen, randnum1,randnum2)
print("Guess which one is higher!\n")
randnum1 = r.randint(0,(spaceobjlen-1))
randnum2 = r.randint(0,(spaceobjlen-1))
input(f"which object is further away from the sun, {data[randnum1]["name"]} or {data[randnum2]["name"]}?\n")
# while ongoing:
#     randnum1 = r.randint(0,(spaceobjlen-1))
#     randnum2 = r.randint(0,(spaceobjlen-1))
#     input(f"which object is further away from the sun, {[randnum1]["name"]} or{[randnum1]["name"]}?\n")
