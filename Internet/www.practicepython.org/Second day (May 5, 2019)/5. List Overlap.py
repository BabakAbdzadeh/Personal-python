# List Overlap
# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# 1.Randomly generate two lists to test this
# 2.Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# help Using Not In On List To Remove Duplicate Elements:
# def duplicate(items):
#     unique = []
#     for item in items:
#         if item not in unique:
#             unique.append(item)
#     return unique


sorted_list = []


def duplicate(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


a_duplicated = duplicate(a)
b_duplicated = duplicate(b)

i = -1
b = 2
sorted_list = []
while b_duplicated and a_duplicated:
    a_min = min(a_duplicated)
    if b_duplicated[i] == min(a_duplicated):
        sorted_list.append(a_min)
        b_duplicated.remove(a_min)
        a_duplicated.remove(a_min)
        i = -1
    elif a_min != b_duplicated[-1]:
        a_duplicated.remove(a_min)
        i = -1

    i = i + 1

print(sorted_list)

print(a_duplicated)
print(b_duplicated)
