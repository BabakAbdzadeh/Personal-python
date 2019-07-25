# Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class. In other
# words, the Dog class does not inherit from the Pets class. Then assign three dog instances to an instance of the
# Pets class. Start with the following code below. Save the file as pets_class.py. Your output should look like this:
#
# I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9.
# And they're all mammals, of course.


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
        for animal in self.dogs:
            print("{} is {} years old".format(animal.name, animal.age))
        print("and they are {}".format(animal.species))


class Dog:
    """
    parent class
    """
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


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


my_dogs = [RussellTerrier("mikey", 5), Bulldog("ted", 3), Dog("john", 7), Bulldog("bahar", 9)]

my_pets = Pet(my_dogs)


print(my_pets.dogs_counter())
print(my_pets.dogs_age())


