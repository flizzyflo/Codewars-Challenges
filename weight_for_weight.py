def order_weight(strng: str) -> list[str]:

    """Sorts and returns a list of integer-strings, sorted by sum of the single string characters and the string to string comparison."""

    strng = sorted(strng.split(" ")) # sort strings beforehand
    return " ".join(sorted([item for item in strng], key= weigh_items)) #return sorted strings, uses weigh_items function as key => sums per string are the key


def weigh_items(string: str) -> int:
    
    """Adds up all characters of an integer string and returns the sum."""

    return sum(int(s) for s in string)
    
