"""Class
A class is a blueprint for the object.
We can think of class as an sketch of a parrot with labels. 
It contains all the details about the name, colors, size etc.
 Based on these descriptions, we can study about the parrot. 
 Here, parrot is an object."""
print("=============Parrot Class Prints:================")
class Parrot:
    #class Attributes
    species = 'bird'

    #instance Attribute
    def __init__(self, name, age):
        self.name= name
        self.age= age

    #instance methods
    def sing(self,song):
        return "{} sings {}".format(self.name,song)

    def dancing_parrot(self):
        return "{} is now a dancing parrot".format(self.name)


#Use That class
blue = Parrot("Blue", 10)
woo = Parrot("Woo",15)

#accessing the classes attributes
print("Blue is a {}".format(blue.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

#access the instance attributes

print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(woo.name, woo.age))
    
#call our instance methods
print(blue.sing("'ye-HAW'"))
print(blue.dancing_parrot())

print("=================Use Of Inheritance====================")
#==========================Use Of Inheritance Python======================++#

print(f"Inheritance is a way of creating\nnew class for using details of\nexisting class without modifying it.\nThe newly formed class is a derived class\n(or child class). Similarly, the existing\nclass is a base class (or parent class).\n")


class Bird:
    def __init__(self):
        print("BIrd is ready to fly my guy")

    def who_am_I(self):
        print("is bird")

    def swim(self):
        print("swim faster bird")

#child class
class Penguin(Bird):
    
    def __init__(self):
        super().__init__()
        print("PENGUIN WILL NOT LOSE THE BATTLE")

    def who_am_I(self):
        print("I am penguin ^.^")

    def run(self):
        print("RUN PENGUIN. BECOME BEST BIRD")
print("running tests...")
penguinNation = Penguin()
penguinNation.who_am_I()
penguinNation.swim()
penguinNation.run()

print("===========Class Encapsulation ==================")

print("Using OOP in Python, we can restrict access \n to methods and variables. This prevent data\nfrom direct modification which is called encapsulation.\n In Python, we denote private attribute using\n underscore as prefix i.e single  _  or double  __ .\n")

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price:{}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price

    
print("running tests...")   
c= Computer()
c.sell()

#changing prine
 
c.__maxprice = 1000
c.sell()

#using the setter function instead

c.setMaxPrice(1000)
c.sell()

"""Output"""
"""Selling Price: 900
Selling Price: 900
Selling Price: 1000"""
#WE have to use a setter function here due to the way we declared
# our __maxprice attribute.

#Initializing a method that way will make it private


print("============Polymorphism==============")
print("Polymorphism is an ability (in OOP) to use common\n interface for multiple form (data types).\n Suppose, we need to color a shape,\n there are multiple shape option (rectangle, square, circle).\n However we could use same method to color any shape. \n This concept is called Polymorphism.\n")

class Rhea:
    def fly(self):
        print("rhea cannot fly my dude")

    def swim(self):
        print("Rhea can't swim")

class PolarBear:
    def fly(self):
        print("Bruh you think these things can fly?")
    
    def swim(self):
        print("Well they can swim...")

#common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
jamies_bird = Rhea()
bryces_bear = PolarBear()


#passing in the cool objec t
print("running tests...")
flying_test(jamies_bird)
flying_test(bryces_bear)
    
    