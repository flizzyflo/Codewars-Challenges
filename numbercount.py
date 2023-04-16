def nb_dig(n, d):
    l = [i ** 2 for i in range(n+1)]
    di = dict()
    for i in l:
        for j in str(i):
            if j in di:
                di[j] += 1
            else:
                di[j] = 1
    return di[str(d)]


print(nb_dig(5750,0))