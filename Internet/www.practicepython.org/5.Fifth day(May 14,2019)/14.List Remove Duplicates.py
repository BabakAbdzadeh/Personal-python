# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


def duplicate_remove(list):
    return list(set(list))
    # list_without_duplicate = []
    # for i in list:
    #     set_organise.add(list[i])
    #
    # for i in set_organise:
    #     list_without_duplicate = set_organise.pop(i)
    # return list_without_duplicate


sample_list = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 8, 7, 6, 5, 4, 3, 0, 0, 0, 0, 22]
print(duplicate_remove(sample_list))
