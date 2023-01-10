
import string

def high(string_to_evaluate: str) -> str:

    """Returns the highest valued word within the string to evaluate. 
    Value depends on position within alphabet."""

    lowercase_letters: str = string.ascii_lowercase
    words: list[str] = string_to_evaluate.split()

    single_letter_values: dict[str, int] = {letter: idx for idx, letter in enumerate(lowercase_letters, 1)}
    word_values: dict[str, int] = {word: 0 for word in words} 
    
    for word in words:
        for letter in word:
            word_values[word] += single_letter_values[letter]
    
    
    return max(word_values, key= lambda key: word_values[key])
    
    