

def is_isogram(string: str) -> bool:
    
    """Checks if every letter occurs just once within the string passed in as argument."""

    return len(set(string.lower())) == len(string)
