def binary_array_to_number(arr: list[int]) -> int:
    
    binary_expression = "".join([str(n) for n in arr])
    
    return int(binary_expression, 2)
