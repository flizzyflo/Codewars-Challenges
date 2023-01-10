
import string 

def is_pangram(strng: str) -> bool:

    """Checks if a given string is a pangram. 
    A pangram is a stream of letters which includes all letters of a given alphabet."""

    alphabet_lower: str = string.ascii_lowercase

    return {letter.lower() for letter in strng if letter.strip() not in string.punctuation} == set(alphabet_lower)



print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
