import re
# 12. Write a Python program that matches a word containing 'z'


def word_match12(string):
    pattern = ''
    if re.search(pattern, string):
        x = re.findall(pattern, string)
        y = re.search(pattern, string)
        print(x,y)
    else:
        print('no match found! ex12')
