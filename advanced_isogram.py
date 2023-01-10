import string

def is_isogram(word: str) -> bool:
    
    if not isinstance(word, str) or not word:
        return False
    
    letter_occurence_dict = count_letters(word.lower())
    
    return same_letter_occurence(letter_occurence_dict)


def count_letters(word: str) -> dict[str, int]:
    
    letter_occurence_dict: dict[str, int] = dict()
    
    for letter in word:
        
        if (letter == "") or (letter == " ") or (letter in string.punctuation):
            continue
        
        elif letter in letter_occurence_dict.keys():
            letter_occurence_dict[letter] += 1

        else:
            letter_occurence_dict[letter] = 1
    
    return letter_occurence_dict
            
            
def same_letter_occurence(letter_occurence_dictionary: dict[str, int]) -> bool:
    
    return len(set(letter_occurence_dictionary.values())) == 1
