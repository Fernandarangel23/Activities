#Dictionaries

Myfirstdictionary = {
    "name": "Fernanda", 
    "age": '24' , 
    'hobbies':['run','watch movies','travel around the world', 'learning new things'], #lista en un diccionario
    'Wake up times': { #diccionario dentro de un diccionario
        '1':'5:30',
        '2':'6:30',
        '3':'10:00'
    }
}

print(f"Hello my name is {Myfirstdictionary['name']}")
print(f"I am {Myfirstdictionary['age']} old")
print(f"I have {len(Myfirstdictionary['hobbies'])} hobbies")
print(f"I wake up at {Myfirstdictionary['Wake up times']['1']}")
