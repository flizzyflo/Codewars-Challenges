def reverse_words(s: str) -> str:
    reverse_string = str()
    wordList = s.split()
    for i in wordList[len(wordList)::-1]:
        reverse_string += i
        reverse_string += " "
        

    return reverse_string.rstrip()

print(reverse_words("das ist super!"))