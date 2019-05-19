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

