def faculty(number: int) -> int:
    
    # recursive basecase 
    if number <= 1:
        return 1
    
    # recursive call
    else:
        # reduces number by 1)
        return number * faculty(number - 1)
