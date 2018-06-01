from utils import is_leaf, is_minimal, is_simple_d, get_neighbour, add_vertex, remove_vertex, add_new_label 

def get_prufer(R, D):
    check_arguments(R, D)
    P = []
    labels = R[:]
    lastNode = max(R)
    while True:
        # S = []
        while R:
            k = min(R)
            m = get_neighbour(k, P, D, labels)
            if m != -1:
                P.append(m)
                D = remove_vertex(D, R, k)
                labels.remove(k)
                R.remove(k)
                if is_simple_d(D):
                    return P
            else:
                lastNode = lastNode + 1
                m = lastNode
                P.append(m)
                D = add_new_label(D, R, k)
                D = remove_vertex(D, R, k)
                labels.remove(k)
                R.remove(k)
                labels.append(m)
                if is_leaf(m, D):
                    R.append(m)
                if is_minimal(R, D):
                    return P
                # S.append(m)
        # R_temp = get_leaves(S, D)
        # if is_minimal(R_temp, D):
        #     break
        # else:
        #     R = R_temp[:]
    
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
