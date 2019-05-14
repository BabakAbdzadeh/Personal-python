# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to
# the user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
#
# Then I would see the string:
#
#   Michele is name My
# shown back to me.


def backward(input_string):
    input_list = input_string.split()
    input_list.reverse()  # input_list.reverse(), like many list methods, acts in-place, and therefore returns None
                          # برای همین اگر سعی کنیم درون یک متغیر قرار دهیم اون متخیر خالی می ماند
    backwardly_list = ' '.join(input_list)
    return backwardly_list


input_var = input("please enter your string:")
print(backward(input_var))
