import sys
import argparse
from algorithm import get_prufer
from prufer import prufer_decode
from utils import matrix_from_csv
from visualize import write_graph

def main():
    parser = argparse.ArgumentParser()
    required_group = parser.add_mutually_exclusive_group(required=True)
    required_group.add_argument("-f", "--file", help="CSV file with distance matrix")
    required_group.add_argument("-d", "--distances", help="Inline distance matrix")
    parser.add_argument("-o", "--output-file", help="Optional output path for .png file with drawn tree")
    args = parser.parse_args()

    try:
        D = []
        if args.file:
            D = matrix_from_csv(args.file)
        if args.distances:
            D = list(eval(args.distances))
    except:
        print("Invalid argument format. Error during parsing distance matrix: {0}".format(sys.exc_info()[0]))
        return

    R = list(range(len(D)))
    P = get_prufer(R, D)
    print("Prüfer sequence: {0}".format(P))
    tree = prufer_decode(P)
    print("Tree edges: {0}".format(tree))

    try:
        if args.output_file:
            write_graph(tree, args.output_file)
    except:
        print("Error writing tree to file: {0}".format(sys.exc_info()[0]))
        return

if __name__ == '__main__':
    main()