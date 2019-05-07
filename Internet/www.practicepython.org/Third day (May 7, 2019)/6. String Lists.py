# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

input_string = input("please type a string :" )
input_list = list(input_string)
input_list_backward = input_list[::-1]
print(input_list_backward)
print(input_list)

if input_list == input_list_backward:
    print("your string is palindrome!")
else:
    print("your string is not palindrome!")


