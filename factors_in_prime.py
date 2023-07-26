def prime_factors(n: int) -> str:
    sqr_root: int = n ** 0.5
    divisor: int = 2
    res: list[str] = list()

    while divisor <= sqr_root:

        power_count: int = 0

        while n % divisor == 0:
            power_count += 1
            n = n // divisor

        if power_count > 1:
            res.append(f"({divisor}**{power_count})")

        if power_count == 1:
            res.append(f"({divisor})")

        divisor += 1

    if n > 1:
        res.append(f"({n})")

    return "".join(res)