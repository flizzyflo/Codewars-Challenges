
from string import ascii_lowercase, ascii_uppercase
from math import ceil
lower_letter_list, upper_letter_list = list(ascii_lowercase), list(ascii_uppercase)
moving_result_string = ""

special_characters = ["â", "(", ")", ".", " ", ",", "!", "?", ";", "-", "_", "´", "'", "é", "è"]
result_list = list()

def appending_decoding_string(index_position: int, letters_to_compare: list, shift: int) -> str:

        """Helper function, which returns string from the right index depending on shift and input letter"""

        if (index_position - shift) >= 0:
            return letters_to_compare[index_position - shift]

        elif (index_position - shift) < 0:
            return letters_to_compare[(len(letters_to_compare) + (index_position - shift)) % len(letters_to_compare)]


def appending_encrypted_string(index_position: int, letters_to_compare: list, shift: int) -> str:

    """Helper function, which returns string from the right index depending on shift and input letter"""

    if (index_position + shift) <= (len(letters_to_compare) - 1):
        return letters_to_compare[index_position + shift]

    elif (index_position + shift) > (len(letters_to_compare) - 1):
        return letters_to_compare[(index_position + shift) % len(letters_to_compare)]


def build_list(initial_string: str) -> list:
    
    """This function translates the string into a list of 5 elements"""
    
    result_list = []
    initial_string_lengt = len(initial_string)
    list_element_lenght = initial_string_lengt / 5

    while len(result_list) <= 4:
        print(initial_string)
        result_list.append(initial_string[:ceil(list_element_lenght)]) 
        initial_string = initial_string[ceil(list_element_lenght):]

    
    return result_list


def moving_shift(s: str, shift: int, special_chars: list = special_characters, shift_increase: bool= False) -> list:

    """This function returns the encrypted string"""

    lower_letter_list, upper_letter_list = list(ascii_lowercase), list(ascii_uppercase)
    moving_result_string = ""
    
    for message_letter in s:  

        if message_letter in special_chars or message_letter.isnumeric() == True:
            moving_result_string += message_letter
        else:
            for index_position, letter in enumerate(lower_letter_list):
                if message_letter.islower() and (message_letter == letter):                           
                    moving_result_string += appending_encrypted_string(index_position, lower_letter_list, shift)

                elif (message_letter.lower() == letter):                                               
                    moving_result_string += appending_encrypted_string(index_position, upper_letter_list, shift)
        if shift_increase:
            shift += 1

    result = build_list(moving_result_string)
    return result


def demoving_shift(s: list, shift: int, special_chars: list = special_characters, shift_increase: bool= False) -> str:

    lower_letter_list, upper_letter_list = list(ascii_lowercase), list(ascii_uppercase)
    demoving_result_string = ""

    for message_letter in "".join(s):

        if message_letter in special_chars or message_letter.isnumeric() == True:
            demoving_result_string += message_letter
        else:
            for index_position, letter in enumerate(lower_letter_list):
                if message_letter.islower() and (message_letter == letter):                   
                    demoving_result_string += appending_decoding_string(index_position, lower_letter_list, shift)

                elif (message_letter.lower() == letter):                                       
                    demoving_result_string += appending_decoding_string(index_position, upper_letter_list, shift)
        if shift_increase:
            shift += 1

    return demoving_result_string

print(demoving_shift("xhehuudvfkxqj", 3, special_characters))
