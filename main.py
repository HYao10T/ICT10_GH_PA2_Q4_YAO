# # Object orieted programming
from pyscript import document, display


# class Section:
#     def __init__(self, numstudents, name, level, adviser):
#         self.numstudents = numstudents # attribute
#         self.name = name               # attribute
#         self.level = level             # attribute
#         self.adviser = adviser         # attribute

# # Instantiating an object
# section1 = Section(24, "Topaz", 10, "Mr. Cortez")
# section2 = Section(25, "Sapphire", 10, "Mr. De Guzman")
# section3 = Section(25, "Ruby", 10, "Mrs. Jimenez")
# section4 = Section(24, "Emerald", 10, "Mr. Calpo")

# # Accessing the attributes of the object
# display(f'{section1.level}-{section1.name} is part of Red Bulldogs', target='output')
# display(f'{section2.level}-{section2.name} is part of Green Hornets', target='output')
# display(f'{section3.level}-{section3.name} is part of Blue Bears', target='output')
# display(f'{section4.level}-{section4.name} is part of Yellow Tigers', target='output')


class Dog: 
    def __init__(self, age, name, owner): 
        self.age = age
        self.name = name
        self.owner = owner

class Breed(Dog): 
    def __init__(self, breed): 
        self.breed = breed

    # Creating a child class
def Submit(e):
    breed = document.getElementById("breed").value
    age = document.getElementById("age").value
    name = document.getElementById("name").value
    owner = document.getElementById("owner").value 

    dog1  = Dog(age, name, owner)
    dog2 = Breed(breed)

    display(f'{dog1.name} is a {dog2.breed} that is {dog1.age} years old and owned by {dog1.owner}', target='output2')
