import unittest
from algorithm import get_prufer

class TestGetPrufer(unittest.TestCase):
    def test_happy_path(self):
        R = [1, 2]
        D = [[0, 2], [2, 0]]
        self.assertEqual(get_prufer(R, D), [3])

    def test_throw_error_on_non_symetrical(self):
        R = [1, 2, 3]
        D = [[0, 1, 3], [2, 0, 3], [3, 3, 0]]
        try:
            self.assertRaises(ValueError, get_prufer(R, D))
        except:
            print("Catched expected exception.")

    def test_throw_error_on_non_zero_diagonal(self):
        R = [1, 2, 3]
        D = [[0, 2, 3], [2, 0, 3], [3, 3, 0]]
        try:
            self.assertRaises(ValueError, get_prufer(R, D))
        except:
            print("Catched expected exception.")

    def test_throw_error_on_invalid_labels(self):
        R = [1, 2]
        D = [[0, 1, 3], [2, 0, 3], [3, 3, 0]]
        try:
            self.assertRaises(ValueError, get_prufer(R, D))
        except:
            print("Catched expected exception.")

    def test_simple_1(self):
        R = [1, 2, 3]
        D = [[0, 2, 3], [2, 0, 3], [3, 3, 0]]
        self.assertEqual(get_prufer(R, D), [4, 4, 5])
    
    def test_simple_2(self):
        R = [1, 2, 3]
        D = [[0, 2, 4], [2, 0, 2], [4, 2, 0]]
        self.assertEqual(get_prufer(R, D), [4, 4, 5])
    
    def test_simple_3(self):
        R = [1, 2, 3, 4]
        D = [[0, 2, 3, 3], [2, 0, 3, 3], [3, 3, 0, 2], [3, 3, 2, 0]]
        self.assertEqual(get_prufer(R, D), [5, 5, 6, 6])

if __name__ == '__main__':
    unittest.main()