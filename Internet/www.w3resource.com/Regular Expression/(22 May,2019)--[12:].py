import re


# 12. Write a Python program that matches a word containing 'z'


def word_match12(string):
    pattern = '\S*[z]\S*'
    if re.search(pattern, string):
        x = re.findall(pattern, string)
        y = re.search(pattern, string)
        print(x, y)
    else:
        print('no match found! ex12')


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
        print(x, y)
    else:
        print('no match found! ex13')


print(word_match13('zoo zebra hazard lampard'
                   'in this string, we have words with Z or oZy like there is a zoo in bazzar'))
