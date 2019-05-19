import re


# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

def match_string9(string):
    pattern = '^a.*b$'
    if re.search(pattern, string):
        x = re.findall(pattern, string)
        y = re.search(pattern, string)
        return x, y
    else:
        return 'no match found! ex9'


print(match_string9('hi'))
print(match_string9('a'))
print(match_string9('ab'))
print(match_string9('abc'))
print(match_string9('aab'))
print(match_string9('aaakjdhfskjsdb'))
print(match_string9('himynameisb'))


#
#
# 10. Write a Python program that matches a word at the beginning of a string.


def word_match10(string):
    pattern = '\A[^\s]*'
    if re.search(pattern, string):
        x = re.findall(pattern, string)
        y = re.search(pattern, string)
        return x, y
    else:
        return 'no match found! ex10'


print(word_match10('hi my name is babak'))
print(word_match10('himy name is babak'))
print(word_match10('himynameisbabak'))

#
#
# 11. Write a Python program that matches a word at end of string, with optional punctuation.


def word_match11(string):
    pattern = '\w+\S*$'
    if re.search(pattern, string):
        x = re.findall(pattern, string)
        y = re.search(pattern, string)
        return x, y
    else:
        return 'no match found! ex11'


print(word_match11('hi my name is babak'))
print(word_match11('hi my name is bakak.'))
print(word_match11('hi my name is nobody else;'))
