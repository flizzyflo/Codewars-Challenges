import math
def normpdf(x: float, mean: float, sd: float) -> float:
    PI: float =math.pi
    var = float(sd) ** 2
    denom = (2*PI*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num / denom

print(normpdf(0.6379,0,1))
