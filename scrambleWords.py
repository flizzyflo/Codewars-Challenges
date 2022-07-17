def scramble(s1: str, s2: str) -> bool:
    
    # if s1 has less letters than s2, s2 can not be arranged out of s1
    if len(s1) < len(s2):
        return False
    
    for letter in s2:
        
        s2_count = s2.count(letter)
        s1_count = s1.count(letter)
        
        # check if letter we are looking for is at least as often as it is in s2 in s1
        if s2_count <= s1_count:
            
            # delete the letter out of the strings as often as it appears, reduces string size
            s2 = s2.replace(letter, "", s2_count)
            s1 = s1.replace(letter, "", s1_count)
            continue
        
        # if letter not in s1, than s2 can not be arranged out of s1; return False
        else:
            return False
    
    return True
