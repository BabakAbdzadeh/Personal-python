# 3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets
# must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

import re


class ValidityOfString:
    def validity(self, input_string):
        pattern_one = '\{.*?\}+?'
        pattern_two = '\[.*?\]+?'
        pattern_three = '\(.*?\)+?'
        a = re.findall(pattern_one, input_string)
        b = re.findall(pattern_two, input_string)
        c = re.findall(pattern_three, input_string)

        return a, b, c


ex_one = ValidityOfString()
print(ex_one.validity('hi (babak) can you {} help me with (some{question}'
                      ') about python ? is { ) refer to something true ? or it should be the same parentheses?'
                      'you can use multiple pattern because of inside loops like (())'
                      'or ({[]})'))
