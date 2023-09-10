def is_palindrome(string: str) -> bool:
""" Checks whether a string passed in as argument is a palindrome or not. 
Returns either true or false, depending on the string.
Example: 
racecar -> true
tree -> false
abbcbba -> true
"""   

    if len(string) <= 1:
        return True
    
    if string[0] != string[-1]:
        return False
        
    cutted_string: str = string[1:len(string)-1] 
    return is_palindrome(cutted_string)
