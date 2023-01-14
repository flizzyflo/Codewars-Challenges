
def count_bits(number: int) -> int:

    """Counts the amount of single bits within the bit representation of the number passed in as argument"""
    
    return bin(number)[2:].count('1')
