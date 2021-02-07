"""
Determine if a string is as permutation of another string.

Complexity:

    Time: O(n log n)
    Space: O(n)
"""

# Compare sorted strings: slow for large strings

class Permutations(object):
    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        return sorted(str1) == sorted(str2)

# Hash Map Lookup: keep track of characters we encounter.
# Time: O(n), Space: O(n)

from collections import defaultdict

class PermutationAlt(object):
    def is_permutation(self, str1, str2):
        if str2 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        unique_counts1 = defaultdict(int)
        unique_counts2 = defaultdict(int)

        for char in str1:
            unique_counts1[char] += 1
        for char in str2:
            unique_counts2[char] += 1
        return unique_counts1 == unique_counts2
