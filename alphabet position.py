import string

def alphabet_position(text: str) -> list[(str, int)]:

    """Insert a string as text. Function will return a list of tuples containing the letter and the position within the alphabet."""

    lower_case_letters: list[str] = [letter for letter in string.ascii_lowercase]
    letter_position: list[int] = {letter: position + 1  for position, letter in enumerate(lower_case_letters)}

    return list((letter, letter_position[letter]) for letter in text.lower() if letter in letter_position.keys())
