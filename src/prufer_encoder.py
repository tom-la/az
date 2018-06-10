
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

def floyd_warshall(edges, k, n):
    int_max = 2147483647
    dist = [[int_max for i in range(n)] for i in range(n)]
    for u in range(n):
        dist[u][u] = 0
    
    for e in edges:
        u, v = e
        dist[u][v] = 1
        dist[v][u] = 1

    for w in range(n):
        for u in range(n):
            for v in range(n):
                if (w == u) or (u == v) or (w == v) or dist[w][u] == 0 or dist[u][v] == 0 or dist[w][v] == 0:
                    continue 
                if dist[u][v] > dist[u][w] + dist[w][v]:
                    dist[u][v] = dist[u][w] + dist[w][v]
                    dist[u][v] = dist[u][w] + dist[w][v]
    
    M = [[0 for i in range(k)] for i in range(k)]
    for i in range(k):
        for j in range(k):
            M[i][j] = dist[i][j]
    return M

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
    D = floyd_warshall(edges, k, n)
    return D
