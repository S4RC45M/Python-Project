import math


def createspaceobject(name,orbityears):
    name = name.capitalize()
    orbityears = round(orbityears)
    return spaceobjects.append({"name": name, "orbityears": orbityears})


spaceobjects = [
    {"name": "Hailey's Comet",
     "orbityears": 76 ,
       },
    {"name": "Jupiter",
        "orbityears": 12,     
       },
    {"name": "Eris",
     "orbityears": 556,
       },
    {"name": "Vesta",
        "orbityears": 4,     
       },
    {"name": "Neptune",
        "orbityears": 165,     
    },
    {
        "name":"Swift-Tuttle",
        "orbityears": 133
    }

]
createspaceobject("Borrelly",6.84)
