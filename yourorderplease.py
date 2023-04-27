def order(sentence: str) -> str:
    sentence = sentence.split(" ")
    letter_dictionary = {}
            
    for list_item in sentence:
        for letter in list_item:
            if letter.isnumeric():
                letter_dictionary[letter] = list_item


    return " ".join([letter_dictionary[key_value] for key_value in sorted(letter_dictionary)])

print(order("is2 Thi1s T4est 3a"))