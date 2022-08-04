

def last_digit(numbers: list) -> int:
    
    """Function grabs last digit of the calculated exponentinal equation and returns it as integer"""
    
    if len(numbers) == 0:
        return 1
    
    # first value within the list is the initial base
    base = numbers[0]
    
    numbers = numbers[1:]
    numbers.reverse()
    total_exponent: int = numbers[0]

    for number in numbers[1:]:
        total_exponent = pow(number, total_exponent)

    # edge case: base is zero, then everytime it will return zero except exponent is zero
    if (base == 0) and (total_exponent == 0):
        return 1

    # base case of base 1 or exponent 0
    elif (base == 1) or (total_exponent == 0):
        return 1
    
    # 1 is always one, independend of the power
    elif total_exponent == 1:
        return base

    else:
        return pow(base, total_exponent, 10)


print(last_digit([2,2,2,0]))