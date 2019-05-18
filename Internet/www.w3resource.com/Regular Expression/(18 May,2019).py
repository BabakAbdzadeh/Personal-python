# hint :
#
# RegEx Functions:
# The "re"  module offers a set of functions that allows us to search a string for a match:
#
# Function:	    Description:
#  1.findall	    Returns a list containing all matches
#  2.search	        Returns a Match object if there is a match anywhere in the string
#  3.split	        Returns a list where the string has been split at each matchRR
#  4.sub	        Replaces one or many matches with a string


# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z,
# A-Z and 0-9)
import re

ex1_string: str = " hi my name is Babak, I am 23 years old , non SERVIAM"
x = re.findall("[a-zA-Z0-9]", ex1_string)
print(x)


#
#
#
# 2. Write a Python program that matches a string that has an a followed by zero or more b's.

def text_match2(string):
    pattern = 'ab*?'
    if re.search(pattern, string):
        return "we have match! ex2"
    else:
        return 'no match found! ex2'


print(text_match2("c"))
print(text_match2("an"))
print(text_match2("anb"))
print(text_match2("hi my name is abbbb"))


#
#
# 3. Write a Python program that matches a string that has an a followed by one or more b's

def text_match3(string):
    pattern = 'ab+?'
    if re.search(pattern, string):
        return 'we have a match! ex3'
    else:
        return 'no match found! ex3'


print(text_match3("a"))
print(text_match3("ab"))


#
#
# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'

def text_match4(string):
    pattern = 'ab?'
    if re.search(pattern, string):
        x = re.search(pattern,string)
        return 'we have a match! ex4', x
    else:
        return 'no match found! ex4'


print(text_match4('a'))
print(text_match4('ab'))
print(text_match4('abbb'))


#
#
# 5. Write a Python program that matches a string that has an a followed by three 'b'

