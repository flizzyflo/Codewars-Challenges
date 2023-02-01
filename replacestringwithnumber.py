def alphabet_position(text: str) -> str:
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index_alphabet, result = dict(), str()
    index = 1
    exception_chars=[",", "'", ".", "-"]
    for letter in alphabet:
        index_alphabet[letter] = index
        index += 1

    for letter in text:
        if letter == " " or letter in exception_chars:
            continue
        # if type(letter) != str():
        #     continue

        result += str(index_alphabet[letter.lower()]) + " "

    return result[:len(result) - 1]

print(alphabet_position("The sunset sets at twelve o' clock."))