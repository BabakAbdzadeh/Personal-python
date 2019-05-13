# Divisors
# Create a program that asks the user for a number and then prints out a list of all the divisors of that
# number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

user_inp = int(input("please enter your wish number: "))
divisors = []
b = 2
# while user_inp % b != 0 and b != 1:
#     b = b + 1
#     if user_inp % b == 0:
#         divisors.append(b)
#         b = b + 1
#     elif user_inp == b:
#         divisors.append(b)
#         b = 1

while user_inp != b:
    if user_inp % b == 0:
        divisors.append(b)
    b = b + 1

if user_inp == 2:
    divisors.append(2)
if user_inp != 2:
    divisors.append(user_inp)
print(divisors)
