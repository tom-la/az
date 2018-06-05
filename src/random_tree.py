
from prufer_encoder import prufer_decode, decode_sequence_to_distance_matrix
import random
import scipy
import scipy.sparse.csgraph
import numpy as np

def tree_to_sequence(tree):
    seq = []
    n = len(tree.keys())
    
    for i in range(n-2):
        leaves = [i for i in tree.keys() if len(tree[i]) == 1]
        if not leaves:
            break
        v = min(leaves)
        seq.append(tree[v][0])
        del tree[v]
        for k in tree.keys():
            try:
                tree[k].remove(v)
            except ValueError:
                pass
    return seq

def random_prufer_sequence(n, l):
    seq = list(range(l, n))
    for _ in range(l - 2):
        seq.append(random.randint(l, n - 1))
    return np.random.permutation(seq).tolist()

def random_tree(n, l):
    sequence = random_prufer_sequence(n, l)
    return sequence

def get_full_distance_matrix(sequence):
    return decode_sequence_to_distance_matrix(sequence)

def random_distance_matrix(n, l):
    seq = random_tree(n, l)
    D = get_full_distance_matrix(seq)
    return D, prufer_decode(seq), seq