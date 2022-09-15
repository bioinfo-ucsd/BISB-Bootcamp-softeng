def calc_hamming_distance(p, q):
    '''
    calculate hamming distance between two strings
    '''

    if (len(p) != len(q)):
        print("lengths are not the same")
        return None
    length = len(p)
    dist = 0
    for i in range(length):
        if (p[i] != q[i]):
            dist += 1

    return dist
