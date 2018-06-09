from utils import is_leaf, is_minimal, is_simple_d, get_neighbour, add_vertex, remove_vertex, add_new_label, get_leaves, is_simple, only_one_leaf

def get_prufer(R, D):
    check_arguments(R, D)
    P = []
    Pn = []
    P_neighbs = []
    labels = R[:]
    lastNode = max(R)
    i = 0
    while True:
        S = []
        while R:
            k = min(R)
            m = get_neighbour(k, P, P_neighbs, D, labels)
            if m != -1:
                P.append(m)
                Pn.append(k)
                D = remove_vertex(D, labels, k)
                labels.remove(k)
                R.remove(k)
            else:
                lastNode = lastNode + 1
                m = lastNode
                P.append(m)
                Pn.append(k)
                D = add_new_label(D, labels, k)
                D = remove_vertex(D, labels, k)
                labels.remove(k)
                R.remove(k)
                labels.append(m)
                S.append(m)
            if len(D) == 2 and D[0][1] == 1:                
                    return [P, Pn]
        if len(labels) >= 1:
            S = list(set(S).union(set(labels)))
        S.sort()
        leaves = get_leaves(S, D, labels)
        if is_simple(leaves, D, labels):
            break
        else:
            R = leaves[:]
    return [P, Pn]

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
