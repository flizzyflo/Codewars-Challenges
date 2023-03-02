
def accum(input_string: str) -> str:

    """
    Function splits string and prints the letter n-times within the new word, where
    n is the index position of the letter wihtin the word, starting with
    index number 1. Capitalizes the first letter of the word if its a letter.
    @param input_string: String of letters and/ or numbers.
    @return: New composed string. 'New' will become 'N-Ee-Www' for example.
    """

    output_string = ""
    for i in range(len(input_string)):
        output_string += (input_string[i] * (i + 1) + "-")
    return output_string.title()[:-1]
