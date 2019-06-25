# 4. Write a Python class to get all possible unique subsets from a set of distinct integers. - Go to the editor
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

from itertools import chain, combinations


class PossibleUniqueSubsets:
    def powerset(self, iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


ex_one = PossibleUniqueSubsets()
print(ex_one.powerset([1, 2, 3]))

