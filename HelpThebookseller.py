
def stock_list(listOfArt: list, listOfCat: list) -> str:

    splitted_articles = []
    stock_dictionary = {}
    result_string =""

    for item in listOfArt:
        splitted_articles.append(item.split(" "))

    for item in splitted_articles:
        if item[0][:1] not in stock_dictionary:
            stock_dictionary[item[0][:1]] = int(item[1])

        else:
            stock_dictionary[item[0][:1]] += int(item[1])


    for letter in listOfCat:
        if letter not in stock_dictionary:
            stock_dictionary[letter] = 0
        
        result_string += f'({letter.capitalize()} : {stock_dictionary[letter]}) - '

    if sum(stock_dictionary.values()) == 0:
        return ""
    else:

        return result_string[:len(result_string) - 3]

