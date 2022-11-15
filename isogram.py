

def is_isogram(string: str) -> bool:
    
    """Checks if every letter occurs just once within the string passed in as argument."""

    string = string.lower()

    for letter in string:
        if string.count(letter) > 1:
            return False

    return True

