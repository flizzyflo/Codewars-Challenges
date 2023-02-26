def iter_pi(epsilon, pi=0, k=0):
    import math
    while math.pi-pi > epsilon:
        pi+=((-1)**k)/(2*k+1)
        k+=1
        if abs(math.pi-(pi*4))<epsilon and k>1:
            return [k,round(pi*4,10)]


print(iter_pi(0.001))


