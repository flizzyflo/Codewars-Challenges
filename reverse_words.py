
def reverse_words(text):
    
    if ("  ") in text:
        return "  ".join([word[::-1] for word in text.split()])

    return " ".join([word[::-1] for word in text.split()])

print(reverse_words("double space"))