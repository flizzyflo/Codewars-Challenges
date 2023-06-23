
def sortme(words):
    words.sort(key=str.lower)
    return words

print(sortme(["Hello", "there", "I'm", "fine"]))