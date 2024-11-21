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
    },
        {
        "name":"Quaoar",
        "orbityears": 289
    },
        {
        "name":"Gonggong",
        "orbityears": 554
    },
        {
        "name":"Tempel 1",
        "orbityears": 6
    },
        {
        "name":"Sedna",
        "orbityears": 11400
    }

]
createspaceobject("Borrelly",6.84)
createspaceobject("Orcus",245)
createspaceobject("Haumea",283.77)