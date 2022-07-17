def generate_hashtag(inputString: str) -> str:
    
    # check for wrong input
    if  140 <= len(inputString) or len(inputString) == 0:
        return False

    # split strings at whitespace
    stringList: list = inputString.split()
    
    # initialize result variable with leading hashtag
    resultString: str = "#"
    
    # add capitalized strings to result string
    for string in stringList:
        resultString += string.capitalize()
        
    return resultString
