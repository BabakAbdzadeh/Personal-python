# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.

# Extras:

# 1.Add on to the previous program by asking the user for another number and printing out that
# many copies of the previous message. (Hint: order of operations exists in Python)
# 2.Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)


name_var = input("please enter your name :")
age_var = int(input("please enter your age:"))
repeat_var = int(input("how many times do you want to see the your last years to 100 sentence?"))
print(str("hi " + name_var + ",in " + str(100 - age_var) + " years you will be 100 years old.\n") * repeat_var)






