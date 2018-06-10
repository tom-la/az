import unittest
import random
from algorithm import get_prufer
from prufer import prufer_decode
from random_tree import random_distance_matrix, tree_to_sequence, is_isomorphic

def get_edges(R, D):
    P, Pn = get_prufer(R, D)
    return prufer_decode(P, Pn)

class TestGetPrufer(unittest.TestCase):
    def test_happy_path(self):
        D = [[0, 2], [2, 0]]
        R = list(range(len(D)))
        self.assertEqual(get_prufer(R, D)[0], [2])

    def test_throw_error_on_non_symetrical(self):
        D = [[0, 1, 3], [2, 0, 3], [3, 3, 0]]
        R = list(range(len(D)))
        try:
            self.assertRaises(ValueError, get_prufer(R, D))
        except:
            print("Catched expected exception.")

    def test_throw_error_on_non_zero_diagonal(self):
        D = [[0, 2, 3], [2, 0, 3], [3, 3, 0]]
        R = list(range(len(D)))
        try:
            self.assertRaises(ValueError, get_prufer(R, D))
        except:
            print("Catched expected exception.")

    def test_throw_error_on_invalid_labels(self):
        D = [[0, 1, 3], [2, 0, 3], [3, 3, 0]]
        R = list(range(len(D)))
        try:
            self.assertRaises(ValueError, get_prufer(R, D))
        except:
            print("Catched expected exception.")

    def test_simple_1(self):
        D = [[0, 2, 2], [2, 0, 2], [2, 2, 0]]
        R = list(range(len(D)))
        P, Pn = get_prufer(R, D)
        self.assertEqual(P, [3, 3])

    def test_simple_2(self):
        D = [[0, 2, 3], [2, 0, 3], [3, 3, 0]]
        R = list(range(len(D)))
        P, Pn = get_prufer(R, D)
        self.assertEqual(P, [3, 3, 4])

    def test_simple_3(self):
        D = [[0, 2, 3, 3], [2, 0, 3, 3], [3, 3, 0, 2], [3, 3, 2, 0]]
        R = list(range(len(D)))
        P, Pn = get_prufer(R, D)
        self.assertEqual(P, [4, 4, 5, 5])

    def test_medium_1(self):
        D = [
            [0, 2, 2, 4, 5, 6, 6, 4],
            [2, 0, 2, 4, 5, 6, 6, 4],
            [2, 2, 0, 4, 5, 6, 6, 4],
            [4, 4, 4, 0, 3, 4, 4, 2],
            [5, 5, 5, 3, 0, 3, 3, 3],
            [6, 6, 6, 4, 3, 0, 2, 4],
            [6, 6, 6, 4, 3, 2, 0, 4],
            [4, 4, 4, 2, 3, 4, 4, 0]
        ]
        R = list(range(len(D)))
        P, Pn = get_prufer(R, D)
        self.assertEqual(P, [8, 8, 8, 9, 10, 11, 11, 9, 12, 10, 9])

    def test_random(self):
        number_of_nodes = range(4, 80, 4)
        number_of_leaves = [random.randint(2, n-2) for n in number_of_nodes]
        param_list = zip(number_of_nodes, number_of_leaves)
        for n, l in param_list:
            with self.subTest(msg="Random distance matrix of tree with {0} nodes, and {1} leaves".format(n, l)):
                D, tree_edges, seq = random_distance_matrix(n, l)
                R = list(range(len(D)))
                computed_tree_edges = get_edges(R, D)
                self.assertTrue(is_isomorphic(tree_edges, computed_tree_edges))

if __name__ == '__main__':
    unittest.main()
