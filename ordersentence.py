

def order(sentence):
    sentence = sentence.split(" ")

    number = [str(x) for x in range(1, 50)]
    temp_list = [word for word in sentence]

    for element in temp_list:
        for char in element:
            if char in number:
                temp_list[int(char) - 1] = element
            else:
                pass

    return " ".join([str(item) for item in temp_list])



print(order("is2 Thi1s T4est 3a"))