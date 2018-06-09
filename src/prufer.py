def prufer_decode(P, Pn):
    # P_copy = P[]
    n = len(P) + 2
    V = list(range(n))
    graph = []
    while P:
        v = find_v(Pn, P)
        p = P[0]
        # connect(graph, v, p)
        graph.append((v, p))
        V.remove(v)
        Pn.remove(v)
        P.remove(p)
    # connect(graph, V[0], V[1])
    graph.append((V[0], V[1]))
    return graph


def find_v(V, P):
    for v in V:
        if v not in P:
            return v

def connect(G, v1, v2):
    G[v1].append(v2)
    G[v2].append(v1)