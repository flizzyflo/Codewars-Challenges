def series_sum(n,s=0,z=1):
    for i in range(n):
        s+=1/(z)
        z+=3
    return ("{:0.2f}".format(s))

print(series_sum(5))
