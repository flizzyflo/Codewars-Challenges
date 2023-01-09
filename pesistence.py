
def persistence(number: int, count: int = 0) -> int:

    """
    Counts the amount of recursive calls until the number is less than 10.
    """

    if number < 10:
        return count

    number = slice_multiplier(number)
    count += 1

    return persistence(number, count)


def slice_multiplier(number_slice: int) -> int:

    """
    Multiplies all digits of a number and returns the sum. 
    E.g. 27 = 2*7 = 14
    """

    number: int = str(number_slice)
    number_slice = int(number[0])

    for slice in number[1:]:
        number_slice *= int(slice)
    
    return number_slice

