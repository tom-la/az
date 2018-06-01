import csv

def is_leaf(m, D):
    return D[-1][-1] == 0

def is_minimal(R, D):
    if len(R) != 2:
        return False
    
    return True

def is_simple_d(D):
    return (len(D) == 2 and D[0][1] == 1) or len(D) < 2

def get_neighbour(v, P, D, labels):
    v_ind = labels.index(v)
    for p in P:
        if p in labels:
            ind = labels.index(p)
            if D[ind][v_ind] == 1:
                return p
    return -1


def add_vertex(G, D):
    old_size = len(G)
    for i in range(old_size):
        if D[-1][i] == 1:
            G[i].append(1)
        else:
            G[i].append(0)
    G.append([1 if D[-1][i] == 1 else 0 for i in range(old_size)])
    return G

def remove_vertex(D, R, k):
    v = R.index(k)
    del D[v]
    for i in range(0, len(D)):
        del D[i][v]
    return D

def add_new_label(D, R, k):
    k_ind = R.index(k)
    old_size = len(D)
    for i in range(old_size):
        D[i].append(0)
    D.append([0 for x in range(old_size + 1)])
    for i in range(old_size):
        new_value = D[i][k_ind] - 1
        if new_value < 0:
            continue
        D[i][old_size] = new_value
        D[old_size][i] = new_value
    return D

def matrix_from_csv(file_path):
    D = []
    with open(file_path, "r") as f: 
        for row in csv.reader(f):
            D.append([int(d) for d in row])
    return D