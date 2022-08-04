
def euklidsAlgorithm(a: int, b: int) -> int:

    """Algorithm takes two integers as input. Calculates the greatest common divisor 
    of both integers"""

    if b > a:
        b, a = a, b

    while True:
        c = a % b

        a = b
        b = c
        
        if c <= 0:
            return a

print("0x2b9")