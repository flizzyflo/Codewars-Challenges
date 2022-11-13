
import string

def high(string_to_evaluate: str) -> str:
    lowercase_letters = string.ascii_lowercase
    single_letter_values: dict[str, int] = dict() 
    words: list[str] = string_to_evaluate.split()
    word_values: dict[str, int] = dict()

    single_letter_values = {letter: idx for idx, letter in enumerate(lowercase_letters, 1)}
    word_values = {word: 0 for word in words} 
    
    for word in words:
        for letter in word:
            word_values[word] += single_letter_values[letter]
    
    
    return max(word_values, key= lambda key: word_values[key])
    
    

print(high("man i need a taxi up to ubud"))
