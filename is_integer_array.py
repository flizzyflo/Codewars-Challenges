

def is_int_array(numbers: list[int]) -> bool:

    """Check whether an array of numbers only has integers in it or not.
    Returns true if it just contains integer, false otherwise."""

    for number in numbers:
        if not isinstance(number, int):
            return False

    return True
