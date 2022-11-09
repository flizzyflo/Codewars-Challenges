
from string import ascii_lowercase

def is_pangram(string: str) -> bool:

    """Checks if a given string is a pangram. A pangram is a stream of letters which includes all letters of a given alphabet."""

    alphabet_lower: str = ascii_lowercase

    for letter in alphabet_lower:
        if letter not in string.lower():
            return False

    return True


# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
