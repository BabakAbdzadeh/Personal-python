# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
# opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in
# the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8,
# 13, …)


def fibonacci(number):
    # a = 1
    # b = 1
    i = 0
    fibonacci_list = [1, 1]
    # for i in number: # i o nemitoone beshbare to number (number int e)
    while i != number - 2:  # -2 bekhatere inke 2 jomle aval too khode list hast
        fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i + 1])
        i += 1
    return fibonacci_list


input_number = int(input("please enter how many Fibonacci numbers you want:"))
print(fibonacci(input_number))
