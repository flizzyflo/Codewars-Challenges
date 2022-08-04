

def last_digit(base: float, exponent: float) -> int:
    
    """Function grabs last digit of the calculated exponentinal equation and returns it as integer"""

    # edge case: base is zero, then everytime it will return zero except exponent is zero
    if (base == 0) and (exponent != 0):
        return 0

    # base case of base 1 or exponent 0
    elif (base == 1) or (exponent == 0):
        return 1
    
    # 1 is always one, independend of the power
    elif exponent == 1:
        return base

    
    else:

        # grabs last number of base 
        string_base = str(base)[-1]
        temporary_exponent = 0

        # iterate over every single number within the exponent
        for iteration in range(len(str(exponent))):
            temporary_exponent = temporary_exponent * 10 + int(str(exponent)[iteration])
            temporary_exponent = temporary_exponent % 4
        
        if temporary_exponent == 0:
            temporary_exponent = 4
   
        return (int(string_base) ** temporary_exponent) % 10
