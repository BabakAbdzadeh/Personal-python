# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
# message to the user.Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# 1.If the number is a multiple of 4, print out a different message.
# 2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

unknown_var = int(input("please insert first number:"))
unknown_var_2 = int(input("please insert second number"))


if unknown_var % unknown_var_2 == 0:
    if unknown_var % 4 == 0:
        print("the", unknown_var, "can be divided by", unknown_var_2, "and it is multiple of 4")
    else:
        print("the", unknown_var, "can be divided by", unknown_var_2)
else:
    print("the", unknown_var, 'can not be divided by', unknown_var_2)
