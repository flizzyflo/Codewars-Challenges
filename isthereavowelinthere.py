def is_vow(inp: list) -> list:
    vowels = ["a", "e", "i", "o", "u"]
    vowel_dict = dict()
    for vowel in vowels:
        vowel_dict[ord(vowel)] = vowel
    
    for index, number in enumerate(inp):
        if number in vowel_dict.keys():
            inp[index] = vowel_dict[number]
    
    return inp
    
    

print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106]))
        
        