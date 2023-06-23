def get_sum(a: int,b: int) -> int:
    if a > b:
        a, b = b, a

        return sum(range(a, b + 1))

    if b < 0 and a > 0:
        return sum(range(b, a + 1)) 

    return sum(range(a, b + 1))

print(get_sum(-5, -1))