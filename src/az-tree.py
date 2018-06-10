import sys
import argparse
from prufer_encoder import decode_sequence_to_distance_matrix
from prufer import prufer_decode
from algorithm import get_prufer
from utils import matrix_from_csv
from visualize import write_graph
from random_tree import random_distance_matrix, is_isomorphic

def edge_list_to_dict(edges):
    tree = {}
    for i, j in edges:
        tree[i] = []
        tree[j] = []
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)
    return tree

def main():
    parser = argparse.ArgumentParser()
    required_group = parser.add_mutually_exclusive_group(required=True)
    required_group.add_argument("-f", "--file", help="CSV file with distance matrix")
    required_group.add_argument("-d", "--distances", help="Inline distance matrix")
    required_group.add_argument("-r", "--random-tree", help="Use random distance matrix with n nodes, and l leafs in format n:l")
    parser.add_argument("-o", "--output-file", help="Optional output path for .png file with drawn tree")
    parser.add_argument("-i", "--test-isomorphism", help="When using random tree as input, test if the original tree is isomorphic to the one reconstructed by the algorithm", action='store_true')
    args = parser.parse_args()

    try:
        D = []
        if args.file:
            D = matrix_from_csv(args.file)
        if args.distances:
            D = list(eval(args.distances))
        if args.random_tree:
            n, l = [int(i) for i in args.random_tree.split(":")]
            if not 2 <= l <= n-1:
                print("Invalid tree parameters: n={0}, l={1}".format(n, l))
                return
            D, tree_random_edges, seq = random_distance_matrix(n, l)
            print("Original Prüfer sequence: {0}".format(seq))
            tree_random = edge_list_to_dict(tree_random_edges)
            print("Original Tree:\n{0}".format(tree_random))
            print("Original Tree edges:\n{0}".format(tree_random_edges))
            try:
                if args.random_tree and args.output_file:
                    write_graph(tree_random, "original-" + args.output_file)
            except:
                print("Error writing tree to file: {0}".format(sys.exc_info()[0]))
                return
    except:
        print("Invalid argument format. Error during parsing distance matrix: {0}".format(sys.exc_info()[0]))
        return
    print("Original matrix:\n{0}".format(D))
    R = list(range(len(D)))
    print(R)
    P, Pn = get_prufer(R, D)
    PCopy = P[:]
    
    print("Prüfer sequence:\n{0}".format(P))
    tree_edges = prufer_decode(P, Pn)
    tree = edge_list_to_dict(tree_edges)
    
    print("Decoded distance matrix:\n{0}".format(decode_sequence_to_distance_matrix(PCopy)))
    if args.random_tree and args.test_isomorphism:
        isomorphic = is_isomorphic(tree_random_edges, tree_edges)
        print("Tree isomorphism test result: {0}".format(isomorphic))

    try:
        if args.output_file:
            write_graph(tree, args.output_file)
    except:
        print("Error writing tree to file: {0}".format(sys.exc_info()[0]))
        return

if __name__ == '__main__':
    main()