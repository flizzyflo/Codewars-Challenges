
def find_it(seq: list[int]) -> list[int]:

    """Loops over an list of integers and returns a generator object containing 
    all the non-odd numbers"""

    yield [x for x in seq if x % 2 != 0 and isinstance(x, int)]

