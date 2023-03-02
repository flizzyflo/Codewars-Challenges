
import string 

def is_pangram(input_string: str) -> bool:

    """Checks if a given string is a pangram. 
    A pangram is a stream of letters which includes all letters of a given alphabet."""

    lowercase_alphabet: str = set(string.ascii_lowercase)
    string_set: str = {letter.lower() for letter in input_string if letter.strip() not in string.punctuation}

    return string_set == lowercase_alphabet
