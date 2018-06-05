import sys
import argparse
from prufer_encoder import prufer_decode, decode_sequence_to_distance_matrix
from algorithm import get_prufer
from utils import matrix_from_csv
from visualize import write_graph
from random_tree import random_distance_matrix, tree_to_sequence
import numpy as np

def node_list_to_dict(nodes):
    tree = {}
    for i, j in nodes:
        tree[i] = []
        tree[j] = []
    for i, j in nodes:
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
    args = parser.parse_args()

    try:
        D = []
        if args.file:
            D = matrix_from_csv(args.file)
        if args.distances:
            D = list(eval(args.distances))
        if args.random_tree:
            n, l = [int(i) for i in args.random_tree.split(":")]
            D, tree_random, seq = random_distance_matrix(n, l)
            print("Original Prüfer sequence: {0}".format(seq))
            tree_random = node_list_to_dict(tree_random)
            print(tree_random)
            if args.random_tree:
                write_graph(tree_random, "original-" + args.output_file)
    except:
        print("Invalid argument format. Error during parsing distance matrix: {0}".format(sys.exc_info()[0]))
        return
    print("Original matrix:\n{0}".format(np.array(D)))
    R = list(range(len(D)))
    print(R)
    P = get_prufer(R, D)
    
    print("Prüfer sequence:\n{0}".format(P))
    tree = prufer_decode(P)
    tree = node_list_to_dict(tree)
    print("Tree edges:\n{0}".format(tree))

    print("Decoded distance matrix:\n{0}".format(np.array(decode_sequence_to_distance_matrix(P))))

    try:
        if args.output_file:
            write_graph(tree, args.output_file)
    except:
        print("Error writing tree to file: {0}".format(sys.exc_info()[0]))
        return

if __name__ == '__main__':
    main()