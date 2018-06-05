import numpy as np
import scipy
import scipy.sparse.csgraph

def get_prufer(R, D):
    check_arguments(R, D)
    D = np.array(D)
    last_node = max(R)
    R = set(R)
    P = []
    while True:
        S = set()
        while len(R) != 0:    
            k = min(R)
            p_i = neighbour(D, P, k)
            if p_i != -1:
                m = p_i
                P.append(m)
                D[k, :] = 0
                D[:, k] = 0
                R.remove(k)
                if (np.count_nonzero(D == 1) <= 2) and (np.count_nonzero(D > 1) == 0):
                    return P
            else:
                last_node += 1
                m = last_node
                P.append(m)

                shape = (D.shape[0]+1, D.shape[0]+1)
                newD = np.zeros(shape, dtype=int)
                newD[0:D.shape[0],0:D.shape[1]] = D
                D = newD

                for i in range(m):
                    d = D[i, k] - 1
                    if d < 0:
                        d = 0
                    D[i, m] = d
                    D[m, i] = d
                
                D[k, :] = 0
                D[:, k] = 0
                R.remove(k)
                S.add(m)

        R_prim = getleaves(S, D)
        if len(R_prim) == 2 and D[R_prim[0], R_prim[1]] == 1:
            return P
        else:
            R = R_prim  
        if len(R) == 0:
            return P
    return P

def check_arguments(R, D):
    len_r = len(R)

    for d_row in D:
        if len(d_row) != len_r:
            raise ValueError("Label list R has inproper length for distance array D.")

    for i in range(0, len_r):
        for j in range(0, len_r):
            if D[i][j] != D[j][i]:
                raise ValueError("Distance matrix D is not symetrical")

    for i in range(0, len_r):
        if D[i][i] != 0:
            raise ValueError("Distance matrix D has not got zeros on main diagonal.")

    for i in range(len_r):
        for j in range(len_r):
            for k in range(len_r):
                if D[i][j] == 0 or D[i][k] == 0 or D[k][j] == 0:
                    continue
                if D[i][j] > D[i][k] + D[k][j]:
                    raise ValueError("Distance matrix D violates triangle inequality: {0}, {1}, {2}".format(D[i][j], D[i][k], D[k][j]))

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

def neighbour(D, P, k):
    for i in P:
        if (D[i, k] == 1 or D[k, i] == 1):
            return i
    return -1

def getleaves(S, D):
    L = S.copy()
    for i in S:
        for j in S:
            for k in S:
                if (i == j) or (i == k) or (j == k):
                    continue
                if (i != j != k) and D[i, j] == D[i, k] + D[k, j]:
                    if k in L:
                        L.remove(k)
    return list(L)
