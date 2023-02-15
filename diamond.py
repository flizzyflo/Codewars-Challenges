
def print_diamond(size: int) -> str:
    """
    Function prints a diamond of size n. n as argument is the amount of lines.
    Only accepts non-odd numbers.
    param: size as integer number
    """

    if not isinstance(size, int) or size % 2 == 0:
        return None

    s = ""
    for a1 in range(1, (size + 1) // 2 + 1):
        for a2 in range((size + 1) // 2 - a1):
            s += " "
        for a3 in range((a1 * 2) - 1):
            s += "*"
        s += "\n"

    for a1 in range((size + 1) // 2 + 1, size + 1):
        for a2 in range(a1 - (size + 1) // 2):
            s += " "
        for a3 in range((size + 1 - a1) * 2 - 1):
            s += "*"
        s += "\n"

    return s
