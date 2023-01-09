def find_multiples(integer: int, limit: int) -> list[int]:

    mult: int = integer
    fact: int = 1
    result: list[int] = list()
    
    while (mult * fact) <= limit:
        result.append(mult * fact)
        fact += 1
    
    return result
