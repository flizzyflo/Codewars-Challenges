def check_string(string: str, ending: str) -> bool:
    
    string_to_compare = string[len(string) - len(ending):]
    return string_to_compare == ending

