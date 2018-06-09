
from prufer_encoder import prufer_decode, decode_sequence_to_distance_matrix
import random
import scipy
import scipy.sparse.csgraph
import numpy as np
import networkx as nx

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

def list_of_edges_to_nx_tree(tree1_edges, tree2_edges):
    tree1 = nx.Graph()
    tree1.add_edges_from(tree1_edges)
    tree2 = nx.Graph()
    tree2.add_edges_from(tree2_edges)
    return tree1, tree2

def is_isomorphic(tree1_edges, tree2_edges):
    tree1, tree2 = list_of_edges_to_nx_tree(tree1_edges, tree2_edges)
    return nx.is_isomorphic(tree1, tree2)

def faster_could_be_isomorphic(tree1_edges, tree2_edges):
    tree1, tree2 = list_of_edges_to_nx_tree(tree1_edges, tree2_edges)
    return nx.faster_could_be_isomorphic(tree1, tree2)