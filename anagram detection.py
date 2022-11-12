# write the function is_anagram
def is_anagram(test: str, original: str) -> bool:
    
    return sorted(test) == sorted(original)

