
def work_on_strings(a: str,b: str) -> str:

    result_a, result_b = str(), str()

    for letter in b:
        if a.lower().count(letter.lower()) % 2 == 0:
            result_b += letter
        
        else:
            result_b += letter.swapcase()

    for letter in a:
        if b.lower().count(letter.lower()) % 2 == 0:
            result_a += letter
        else:
            result_a += letter.swapcase()

    
    result_string = result_a + result_b
    return result_string


print(work_on_strings("abcdeFg", "defgG"))
