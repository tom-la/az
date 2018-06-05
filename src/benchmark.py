import sys
import argparse
import time
import random
from algorithm import get_prufer
from prufer_encoder import prufer_decode, decode_sequence_to_distance_matrix
from random_tree import random_distance_matrix, tree_to_sequence
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import floor
start_time = time.time()


def range_of_length(start, stop, length):
    return np.floor(np.linspace(start=start, stop=stop, num=length)).astype(int)

def main():
    n_max = 100
    n_start = 10
    step = 10
    ntests = 5
    ncases = len(list(range(n_start, n_max, step)))

    results = []

    for n in range(n_start, n_max, step):
        subresults = []
        for l in range_of_length(2, n-2, ntests):
            if n <= 3:
                l = n - 1

            D, _, _ = random_distance_matrix(n, l)
            R = list(range(len(D)))

            start_time = time.time()
            get_prufer(R, D)
            execution_time = time.time() - start_time

            print("--- %s, %s, %s seconds ---" % (n, l, execution_time))
            subresults.append(execution_time)
        results.append(np.mean(subresults))

    print(results)
    plt.plot(list(range(ncases)), results, 'ro')
    fig = plt.gcf()
    plt.show(block=True)
    fig.savefig('benchmark.png')


if __name__ == '__main__':
    main()
