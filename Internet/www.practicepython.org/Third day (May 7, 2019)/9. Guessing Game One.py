# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the
# very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random
random_number = random.randint(1, 9)
i = 0
while True:

    input_string = input("please Enter your number: ")
#i put exit first because of int and string problems
    if input_string == "Exit" or input_string == "exit":
        print("thanks for playing you did ", i, "tries")
        break
"""
اجبارن دستور خروج و اول گذاشتم ،چون اگه کاربر خروج ارور میداد که
نمیشه کاراکتر و به رقم (int) تبدیل کرد
"""
    input_number = int(input_string)
    i = i + 1
    if input_number == random_number:
        print(" your guess is right the number is ", input_number, "and you did ", i, "tries")
        random_number = random.randint(1, 9)
        print("number has been changed , guess the new number")

    elif input_number < random_number:
        print("go up your guess is low")
    else:
        print("go down you guess is high")

