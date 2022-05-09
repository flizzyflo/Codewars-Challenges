from functools import lru_cache

@lru_cache(10)
def fibonacci(n):
    if n < 1:
        raise IOError(f"wrong input, '{n}' is lower than minimum value of 1. Please adjust.")

    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
