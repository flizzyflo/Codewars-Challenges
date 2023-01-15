def sum_pairs(ints, s, a=[]):
    i=0
    for i,j in enumerate(ints):
        for k,l in enumerate(ints):
            if j+l==s and k>i and k>i:
                a.append([i,k])


    return a
