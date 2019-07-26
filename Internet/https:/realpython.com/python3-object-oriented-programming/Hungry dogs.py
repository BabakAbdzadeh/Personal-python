# Using the same file, add an instance attribute of is_hungry = True to the Dog class. Then add a method called eat()
# which changes the value of is_hungry to False when called. Figure out the best way to feed each dog and then output
# “My dogs are hungry.” if all are hungry or “My dogs are not hungry.” if all are not hungry. The final output should
# look like this:
#
# I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9.
# And they're all mammals, of course.
# My dogs are not hungry.


# Next, add a walk() method to both the Pets and Dog classes so that when you call the method on the Pets class,
# each dog instance assigned to the Pets class will walk(). Save this as dog_walking.py. This is slightly more
# difficult.
#
# Start by implementing the method in the same manner as the speak() method. As for the method in the Pets class,
# you will need to iterate through the list of dogs, then call the method itself.
#
# The output should look like this:
#
# Tom is walking!
# Fletcher is walking!
# Larry is walking!


class Pet:
    """
    parent class
    """

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def dogs_counter(self):
        return "I have {} dogs".format(len(self.dogs))

    def dogs_age(self):
        global animal
        for animal in self.dogs:
            print("{} is {} years old".format(animal.name, animal.age))
        print("and they are {}, of course".format(animal.species))

    def dogs_hunger(self):

        are_my_dogs_hungry = False
        for dog in self.dogs:
            if dog.is_hungry:
                are_my_dogs_hungry = True
        if are_my_dogs_hungry:
            print("my dogs are hungry")
        else:
            print("My dogs are not hungry")

    def walk(self):
        for dog in self.dogs:
            print("{} is walking".format(dog.name))


class Dog:
    """
    parent class
    """
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False

    def hungry_statement(self):
        if not self.is_hungry:
            return "my dogs are not hungry"
        else:
            return "my dogs are hungry"

    def walk(self):
        return "{} is walking ".format(self.name)


class RussellTerrier(Dog):
    """
    child class
    """

    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Bulldog(Dog):
    """
    child class
    """

    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


my_dogs = [RussellTerrier("mikey", 5), Bulldog("ted", 3), Dog("john", 7), Bulldog("rexbull", 9)]

my_pets = Pet(my_dogs)

print(my_pets.dogs_counter())
print(my_pets.dogs_age())

print(my_pets.dogs_hunger())
print(my_pets.walk())

print(my_dogs[0].walk())
