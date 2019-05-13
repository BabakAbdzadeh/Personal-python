# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions


def prime(number):
    i = 2
    while number % i != 0:
        i += 1
    if i == number:
        return number
    else:
        return 'its not prime'


number_input = int(input("please enter your number:"))

if prime(number_input) == 'its not prime':
    print(number_input, "is not prime")
else:
    print(prime(number_input), "is prime number")
