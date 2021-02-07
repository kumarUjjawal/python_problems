# Implement Fizz Buzz

""" 
What is fuzz buzz?
  Return the string representation of numbers from 1 to n
  multiples of 3: fizz
  mulitples of 5: buzz
  multiples of 3 and 5: fizzbuzz

  > Time: O(n)
  > Space: O(n)

"""

class Solution(object):
    def fizz_buzz(self, num):
        if num is None:
            raise TypeError('num can not be none')
        if num < 1:
            raise ValueError('num can not be less than one')
        results = []
        for i in range(1, num+1):
            if i % 3 == 0 and i % 5 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return results

# Unit Test

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.fizz_buzz, None)
        self.assertRaises(ValueError, solution.fizz_buzz, 0)
        expected = [
                '1',
                '2',
                'Fizz',
                '4',
                'Buzz',
                'Fizz',
                '7',
                '8',
                'Fizz',
                'Buzz',
                '11',
                'Fizz',
                '13',
                '14',
                'FizzBuzz'
                ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')

def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()

if __name__ == '__main__':
    main()
