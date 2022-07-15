def romanLetterCounter(romanLetters: str) -> int:

    # store letter values in dictionary
    romanLetterValues: dict[str, int] = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    # initialize resultcounter
    result: int = 0
    
    for idx, romanLetter in enumerate(romanLetters):
    
        # edge case: letter needs to be subtracted
        # if letter value is lower than next letter value, it needs to be subtracted
        
        # end of romanLetters is reached; full value can be added
        if idx + 1 == len(romanLetters):
            result += romanLetterValues[romanLetter]
        
        elif romanLetterValues[romanLetter] >= romanLetterValues[romanLetters[idx + 1]]:
            # adding the value of the letter to the result. next letter is lower than current
            result += romanLetterValues[romanLetter]
        else:
            # subtracting letter value, since the next letter value is higher than current
            result -= romanLetterValues[romanLetter]
            
    return result
