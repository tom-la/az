
from prufer_encoder import prufer_decode, decode_sequence_to_distance_matrix
import random
from operator import itemgetter
#import networkx as nx
from chempy.graph import Graph, Edge, Vertex

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
    random.shuffle(seq)
    return seq

def random_tree(n, l):
    sequence = random_prufer_sequence(n, l)
    return sequence

def get_full_distance_matrix(sequence):
    return decode_sequence_to_distance_matrix(sequence)

def random_distance_matrix(n, l):
    seq = random_tree(n, l)
    D = get_full_distance_matrix(seq)
    return D, prufer_decode(seq), seq

def tree_from_list_of_edges(tree_edges):
    n = max([max(i, j) for i, j in tree_edges]) + 1
    vertices = [Vertex() for i in range(n)]
    edges = [Edge() for i in range(n)]
    tree = Graph()
    for vertex in vertices: tree.addVertex(vertex)
    k = 0
    for i, j in tree_edges:
        tree.addEdge(vertices[i], vertices[j], edges[k])
        tree.addEdge(vertices[j], vertices[i], edges[k])
        k += 1
    return tree

def is_isomorphic(tree1_edges, tree2_edges):
    tree1, tree2 = tree_from_list_of_edges(tree1_edges), tree_from_list_of_edges(tree2_edges)
    return tree1.isIsomorphic(tree2)

# def faster_could_be_isomorphic(tree1_edges, tree2_edges):
#     tree1, tree2 = list_of_edges_to_nx_tree(tree1_edges, tree2_edges)
#     return nx.faster_could_be_isomorphic(tree1, tree2)