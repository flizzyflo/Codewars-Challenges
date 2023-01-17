
def nb_year(p0: int, percent: int, aug: int, p: int, count: int= 0) -> int:

    if p0 >= p:
        return count
    
    p0 = int(p0 *(1 + percent / 100) + aug)
    count += 1

    return nb_year(p0, percent, aug, p, count)
        