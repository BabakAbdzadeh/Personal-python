# Using the same Dog class, instantiate three new dogs, each with a different age. Then write a function called,
# get_biggest_number(), that takes any number of ages (*args) and returns the oldest one. Then output the age of the
# oldest dog like so:
#
# The oldest dog is 7 years old.
from typing import List, Any


class Dog:
    dog_list = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.dog_list.append(self.name)
        Dog.dog_list.append(self.age)

    def get_biggest_number(*args):

        print("The oldest dog is {} years old.".format(
            max(args)))


mikey = Dog("mikey", 5)
ted = Dog("ted", 7)
rex = Dog("rex", 3)

Dog.get_biggest_number(mikey.age, ted.age, rex.age)