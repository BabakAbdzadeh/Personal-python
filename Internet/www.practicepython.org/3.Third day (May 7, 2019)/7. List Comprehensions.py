# Let’s say I give you a list saved in a variable:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# .Write ONE line of
# Python that takes this list a and makes a new list that has only the even elements of this list in it.

"""
lets try with new random list
"""
import random

numlist = []
list_length = random.randint(5, 15)

while len(numlist) < list_length:
    numlist.append(random.randint(1, 75))
"""
One line Code for finding Even numbers
"""

evenlist = [number for number in numlist if number % 2 == 0]

print("even numbers are:", evenlist)
