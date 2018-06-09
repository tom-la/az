import unittest
from prufer_encoder import decode_sequence_to_distance_matrix
import numpy as np
import copy
import numpy.testing as npt
import random
from algorithm import get_prufer
from prufer import prufer_decode
from random_tree import random_distance_matrix, tree_to_sequence, is_isomorphic, faster_could_be_isomorphic


def get_matrices(R, D):
    DCopy = copy.deepcopy(D)
    P, Pn = get_prufer(R, D)
    DComputed = decode_sequence_to_distance_matrix(P)
    return [DCopy, DComputed]

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
        D = [[0, 2, 3], [2, 0, 3], [3, 3, 0]]
        R = list(range(len(D)))
        Doriginal, DComputed = get_matrices(R, D)
        npt.assert_array_equal(Doriginal, DComputed)

    def test_simple_2(self):
        D = [[0, 2, 3], [2, 0, 3], [3, 3, 0]]
        R = list(range(len(D)))
        Doriginal, DComputed = get_matrices(R, D)
        npt.assert_array_equal(Doriginal, DComputed)

    def test_simple_3(self):
        D = [[0, 2, 3, 3], [2, 0, 3, 3], [3, 3, 0, 2], [3, 3, 2, 0]]
        R = list(range(len(D)))
        Doriginal, DComputed = get_matrices(R, D)
        npt.assert_array_equal(Doriginal, DComputed)

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
        Doriginal, DComputed = get_matrices(R, D)
        npt.assert_array_equal(Doriginal, DComputed)

    def test_random(self):
        number_of_nodes = range(4, 80, 4)
        number_of_leaves = [random.randint(2, n-2) for n in number_of_nodes]
        param_list = zip(number_of_nodes, number_of_leaves)
        for n, l in param_list:
            with self.subTest(msg="Random distance matrix of tree with {0} nodes, and {1} leaves".format(n, l)):
                D, tree_edges, seq = random_distance_matrix(n, l)
                R = list(range(len(D)))
                computed_tree_edges = get_edges(R, D)
                if not faster_could_be_isomorphic(tree_edges, computed_tree_edges):
                    self.fail("Trees are not isomorphic")
                self.assertTrue(is_isomorphic(tree_edges, computed_tree_edges))

if __name__ == '__main__':
    unittest.main()
