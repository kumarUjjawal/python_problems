""" Perform Insertion Sort

    Time: O(n^2) average, worst. 
          O(1) best if the input is already sorted
    Space: O(1) for the iterative solution

"""

class InsertionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be none')
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    temp = data[r]
                    data[l+1:r+1] = data[l:r]
                    data[l] = temp
        return data


# Unit Test

import unittest

class TestInsertionSort(unittest.TestCase):
    def test_sort(self):
        insertion_sort = InsertionSort()

        print('None input')
        self.assertRaises(TypeError,insertion_sort.sort, None)

        print('Empty input')
        self.assertEqual(insertion_sort.sort([]), [])

        print('One Element')
        self.assertEqual(insertion_sort.sort([5]), [5])

        print('Two or more elements')
        data = [5,1,7,2,6,-3,5,7,-1]
        self.assertEqual(insertion_sort.sort(data), sorted(data))

        print('Success: test_insertion_sort')

def main():
    test = TestInsertionSort()
    test.test_insertion_sort()

if __name__ == '__main__':
    main()
