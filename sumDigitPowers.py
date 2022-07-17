def sum_dig_pow(a: int, b: int) -> list: 
    
    resultList: list[int] = []
    tempResult: int = 0
    
    for power, number in enumerate(range(a, b + 1), 1):
        
        # Case of single digit numbers; always are theirselves.
        if 0 < number < 10:
            resultList.append(number)
        
        # number is at least 10 or bigger
        else:
            
            # iterate over the single digits of the number bigger than 10
            for pow, num in enumerate(str(number), 1):
                tempResult += int(num) ** pow
            
            # check if the sum of powers of the single digits equals the initial number
            if tempResult == number:
                resultList.append(tempResult)
            
            # reset temporary variable for next iteration
            tempResult = 0
            
    return resultList
