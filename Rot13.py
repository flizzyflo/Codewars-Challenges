from string import ascii_lowercase, ascii_uppercase
lower_case = ascii_lowercase
upper_case = ascii_uppercase

def rot13(message: str, shift: int = 13) -> str:
    result_string = ""
    

    for original_letter in message:

        # # #exception sonderzeichen
        if original_letter not in lower_case and original_letter not in upper_case:
            result_string += original_letter
    
        #normaler fall
        index_position = lower_case.find(original_letter.lower())

        if index_position + shift > len(lower_case):
            index_position = index_position + shift - len(lower_case)
        
        else:
            index_position += shift

        try:
            if original_letter in ascii_lowercase:
                result_string += ascii_lowercase[abs(index_position)]

            elif original_letter in ascii_uppercase:
                result_string += ascii_uppercase[abs(index_position)]
        except:
            if original_letter in ascii_lowercase:
                result_string += "a"
            elif original_letter in ascii_uppercase:
                result_string += "A"

    return result_string

print(rot13("nTest22"))
