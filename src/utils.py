import csv

def is_leaf(m, D):
    len_D = len(D)
    # print(D)
    for i in range(len_D-1):
        for j in range(len_D-1):
            if (not (i == j == -1)) and D[i][j] == D[i][-1] + D[-1][j]:
                return False
    return True

def is_minimal(R, D):
    if len(R) != 2:
        return False
    
    return True

def only_one_leaf(D, labels, m, R):
    i = labels.index(m)
    has_single_one = False
    for j in range(len(D)):
        if D[i][j] == 1:
            if has_single_one:
                return False
            else:
                has_single_one = True
    return has_single_one

# TODO: cleanup
def is_simple_d(D):
    return (len(D) == 2 and D[0][1] == 1) or len(D) < 2
    # len_D = len(D)
    # if (len_D < 2):
    #     return True

    # has_single_one = False
    # for i in range(len_D):
    #     for j in range(i+1, len_D):
    #         if D[i][j] == 1:
    #             if has_single_one:
    #                 return False
    #             else:
    #                 has_single_one = True
    # return has_single_one

# TODO: ckeanup
def get_leaves(S, D, labels):
    len_D = len(D)
    leaves = S[:]
    # print(S)
    # print(D)
    for i in range(len_D):
        for j in range(len_D):
            for k in range(len_D):
                if (i == j) or (i == k) or (j == k):
                    continue 
                if (i != j != k) and D[i][j] == D[i][k] + D[k][j]:
                    # print("Match: {} {} {}".format(i, j, k))
                    if labels[k] in leaves:
                        # print("Removing {}".format(labels[k]))
                        leaves.remove(labels[k])
    return leaves

def is_simple(leaves, D, labels):
    # if len(leaves) == 0:
    #     return True
    if len(leaves) == 1 and len(D) == 1 and D[0][0] == 0:
        return True

    if len(leaves) != 2:
        return False

    l1 = labels.index(leaves[0])
    l2 = labels.index(leaves[1])
    return D[l1][l2] == 1

def get_neighbour(v, P, P_neighbs, D, labels):
    v_ind = labels.index(v)
    for p in P:
        if p in labels:
            ind = labels.index(p)
            if D[ind][v_ind] == 1:
                return p
    # for i in range(len(P)):
    #     if P[i] == v:
    #         if P_neighbs[i] in P:
    #             return P_neighbs[i]
                
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

def remove_vertex(D, labels, k):
    v = labels.index(k)
    del D[v]
    for i in range(0, len(D)):
        del D[i][v]
    return D

def add_new_label(D, labels, k):
    k_ind = labels.index(k)
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