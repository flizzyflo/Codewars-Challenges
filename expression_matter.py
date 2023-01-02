
def expression_matter(a: int, b: int, c: int) -> int:
    
    if 1 in [a, b, c]:
        s = sum(number for number in [a, b, c] if number == 1)
        return s * c 
    
    else:
        return a * b * c