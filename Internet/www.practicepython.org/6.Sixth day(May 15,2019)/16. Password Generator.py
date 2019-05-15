# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
# password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import random
from typing import List


def password_generator(length, strong):
    global pass_gen
    lowercase_letter = []
    uppercase_letter = []
    pass_list: List[str] = []
    i = 0

    for letter in range(97, 123):
        lowercase_letter.append(chr(letter))
    for letter in range(65, 91):
        uppercase_letter.append(chr(letter))

    letter_list = lowercase_letter + uppercase_letter

    while length >= i:
        if strong == "3":
            i += 2
            first = str(letter_list[random.randint(0, 51)])
            second = str(random.randint(0, 9))
            pass_gen = first + second

        elif strong == "2":
            i += 3
            first = str(letter_list[random.randint(0, 51)])
            second = str(random.randint(0, 9))
            third = str(random.randint(0, 9))
            pass_gen = first + second + third

        elif strong == "1":
            i += 4
            first = str(letter_list[random.randint(0, 51)])
            second = str(random.randint(0, 9))
            third = str(random.randint(0, 9))
            fourth = str(random.randint(0, 9))
            pass_gen = first + second + third + fourth
        pass_list.append(pass_gen)

    generated_password = ''.join(pass_list)

    return generated_password[:length]


length_input = int(input("please Enter the length of your password:"))
strength_input = str(input("please Enter the strength of you password from 1 to 3 ( 3 is strongest):"))

print("your password is:", password_generator(length_input, strength_input))
