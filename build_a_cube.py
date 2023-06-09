def find_nb(m, cube=0,n=0):
    while cube<m:
        cube+=abs(n**3)
        n-=1
    if cube!=int(m):
        return -1
    else:
        return abs(n+1)


print(find_nb(4183059834009))