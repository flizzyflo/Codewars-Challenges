
def mxdiflg(a1: list[str], a2: list[str]) -> int:

    """
    Return the maximum difference between word lengths within both lists passed in as arguments.
    """

    if not a1 or not a2:
        return -1

    a = abs(min(len(string) for string in a1) - max(len(string) for string in a2))
    b = abs(min(len(string) for string in a2) - max(len(string) for string in a1))

    return max(a, b)
