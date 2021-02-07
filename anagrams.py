# Sort an array of string so all anagrams are next to each other

""" Time: O(k*n)
    Space: O(n)
"""

from collections import OrderedDict

class Anagram(object):

    def group_anagram(self, items):
        if items is None:
            raise TypeError("items can not be none.")
        if not items:
            return items
        anagram_map = OrderedDict()
        for item in items:
            sorted_chars = tuple(sorted(item))
            if sorted_chars in anagram_map:
                anagram_map[sorted_chars].append(item)
            else:
                anagram_map[sorted_chars] = [item]
        result = []
        for value in anagram_map.values():
            result.extend(value)
        return result

# Unit Test

import unittest

class TestAnagram(unittest.TestCase):
    def test_group_anagrams(self):
        anagram = Anagram()
        self.assertRaises(TypeError, anagram.group_anagram, None)
        data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
        expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
        self.assertEqual(anagram.group_anagram(data), expected)

        print('Success: test_group_anagrams')

def main():
    test = TestAnagram()
    test.test_group_anagrams()

if __name__ == '__main__':
    main()
