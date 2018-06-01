def prufer_decode(P):
    # P_copy = P[]
    n = len(P) + 2
    V = list(range(n))
    graph = { v: [] for v in range(n) }
    while P:
        v = find_v(V, P)
        p = P[0]
        connect(graph, v, p)
        V.remove(v)
        P.remove(p)
    connect(graph, V[0], V[1])
    return graph

def find_v(V, P):
    for v in V:
        if v not in P:
            return v

def connect(G, v1, v2):
    G[v1].append(v2)
    G[v2].append(v1)