import string


def is_isogram(word: str) -> bool:
    
    if not isinstance(word, str) or not word:
        return False
    
    letter_occurrence_dict = count_letters(word.lower())
    
    return same_letter_occurrence(letter_occurrence_dict)


def count_letters(word: str) -> dict[str, int]:
    
    letter_occurrence_dict: dict[str, int] = dict()
    
    for letter in word:
        
        if (letter == "") or (letter == " ") or (letter in string.punctuation):
            continue
        
        elif letter in letter_occurrence_dict.keys():
            letter_occurrence_dict[letter] += 1

        else:
            letter_occurrence_dict[letter] = 1
    
    return letter_occurrence_dict
            
            
def same_letter_occurrence(letter_occurrence_dictionary: dict[str, int]) -> bool:
    
    return len(set(letter_occurrence_dictionary.values())) == 1
