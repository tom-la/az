import numpy as np
import scipy
import scipy.sparse.csgraph

def prufer_decode(P):
    n = len(P) + 2
    V = set(range(n))
    E = [None]*(n-1)
    for i in range(0, n-2):
        v = None
        for ver in V:
            if not ver in P[i:]:
                v = ver
                break
        E[i] = (v, P[i])
        V.remove(v)
    E[n-2] = (V.pop(), V.pop())
    return E

def decode_sequence_to_distance_matrix(sequence):
    edges = prufer_decode(sequence)
    n = 0
    for e in edges:
        i, j = e
        n = max([n, i, j])
    n = n + 1

    if not sequence:
        k = 2
    else:
        k = min(sequence)

    AdjacencyMatrix = [[0] * n for i in range(n)]
    for e in edges:
        i, j = e
        AdjacencyMatrix[i][j] = 1
        AdjacencyMatrix[j][i] = 1
    D = scipy.sparse.csgraph.floyd_warshall(AdjacencyMatrix, directed=False, unweighted=True)
    D = D[0:k, 0:k].astype(int).tolist()
    return D
