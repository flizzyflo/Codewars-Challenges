def gimme(input_array: list):
    
    s = sorted(input_array)
    
    idx = len(s) // 2
    val = s[idx]
    return input_array.index(val)
