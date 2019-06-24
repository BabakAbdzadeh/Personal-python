import re


# 12. Write a Python program that matches a word containing 'z'


def word_match12(string):
    pattern = '\S*[z]\S*'
    if re.search(pattern, string):
        x = re.findall(pattern, string)
        y = re.search(pattern, string)
        return x, y
    else:
        return 'no match found! ex12'


print(word_match12('babak'))
print(word_match12('zoo'))
print(word_match12('hazard'))
print(word_match12('in this string we have words with Z like there is a zoo in bazar'))


#
# 13. Write a Python program that matches a word containing 'z', not start or end of the word.

def word_match13(string):
    pattern = '\S*\B[z,Z]\B\S*'
    if re.search(pattern, string):
        x = re.findall(pattern, string)
        y = re.search(pattern, string)
        return x, y
    else:
        return 'no match found! ex13'


print(word_match13('zoo zebra hazard lampard'
                   'in this string, we have words with Z or oZy like there is a zoo in bazzar'))


#
# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

def word_match14(string):
    pattern = '^[a-zA-Z0-9_]*$'
    if re.search(pattern, string):
        x = re.findall(pattern, string)
        y = re.search(pattern, string)
        return x, y
    else:
        return 'no match found! ex14'


print(word_match14('zoo zebra hazard lampard'
                   'in this string, we have words with Z or oZy like there is a zoo in bazzar'))
print(word_match14('this_is_a_test_for_SEEing_its_workingOrNot'))


#
# 15.