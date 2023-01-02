
def get_middle(string: str) -> str:
    
    # length is odd
    if len(string) % 2 == 0:
        length = len(string) // 2 - 1
        return string[length:length + 2] 

    # length is not odd, just single middle character is returned
    else:
        return string[len(string)//2]