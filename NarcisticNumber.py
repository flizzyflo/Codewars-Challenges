def narcissistic(value: int):
    
    power: int = len(str(value))  # store the lenght of the number, since it is used as power
    result: int = 0
    
    # grab single number out of the input
    for number in str(value):
        result += int(number) ** power
    
    return result == value