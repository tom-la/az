import sys
import argparse
import time
import random
from algorithm import get_prufer
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

    results_df = pd.DataFrame({'n':  pd.Series(dtype=np.int32), 'l':  pd.Series(dtype=np.int32), 'running_time':  pd.Series(dtype=np.float)},
        columns=['n', 'l', 'running_time'])
    i = 0
    for n in range(n_start, n_max, step):
        for l in range_of_length(2, n-2, ntests):
            i += 1
            if n <= 3:
                l = n - 1

            D, _, _ = random_distance_matrix(n, l)
            R = list(range(len(D)))

            start_time = time.time()
            get_prufer(R, D)
            execution_time = time.time() - start_time

            print("--- %s, %s, %s seconds ---" % (n, l, execution_time))
            results_df.loc[i,:] = (n, l, execution_time)

    mean_running_time_per_node_num = results_df.groupby('n').mean().loc[:,'running_time']
    mean_running_time_per_node_num.plot()
    fig = plt.gcf()
    plt.title('Running time of the algorithm with different number of nodes')
    plt.xlabel('Number of nodes in a tree')
    plt.ylabel('Mean running time of the algorithm [s]')
    fig.savefig('benchmark.png')
    results_df.to_csv('benchmark.csv', index=False)

if __name__ == '__main__':
    main()
