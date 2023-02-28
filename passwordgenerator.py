from random import randint
import string


def generate_password(desired_password_length: int, use_characters_just_once: bool = True) -> str:

    """
    Generates a password consisting out of several elements from lower- and uppercase,
    digits and punctuation elements

    @param desired_password_length: Specifies the length of the password.
    Current max length: 94 characters if character is allowed to be used once

    @param use_characters_just_once: Default True, specifies if characters
    are allowed to be used once or unlimited during password creation
    @return: generated password as string.
    """
    
    minimum_password_length: int = 8
    all_relevant_characters: list[str] = [string.digits, string.ascii_lowercase, string.punctuation, string.ascii_uppercase]
    max_password_length: int = sum(len(character_count) for character_count in all_relevant_characters)

    if desired_password_length < minimum_password_length:
        return f"Password is to short to be considered secure. Minimum length is '{minimum_password_length}' characters to be considered secure."
    
    elif desired_password_length > max_password_length and use_characters_just_once:
        return f"Desired password length '{desired_password_length}' characters is too long.\nMaximum length is '{max_password_length}' characters using every character once."

    password: str = ""
    current_password_length: int = len(password)
    variety_counter: int = 0

    while current_password_length < desired_password_length:

        if variety_counter < len(all_relevant_characters) - 1:
            # if statement is false as long as not at least one letter from every letter type is used
            # ensures that a character from every single type of characters is included into password
            
            letter_category = variety_counter
            variety_counter += 1

        else:
            # random selection of remaining characters to complete the password 
            
            letter_category = randint(0, len(all_relevant_characters) - 1)

        # selection of the letter out of the string
        letter_index = randint(0, len(all_relevant_characters[letter_category]) - 1)

        # store selected letter
        letter_to_add = all_relevant_characters[letter_category][letter_index]

        if letter_to_add not in password and use_characters_just_once:
            # checks if letter is already used for password, 
            password += all_relevant_characters[letter_category][letter_index]
            current_password_length = len(password)

        elif not use_characters_just_once:
            # if characters are allowed to be used more than once
            password += all_relevant_characters[letter_category][letter_index]
            current_password_length = len(password)
        
        else:
            continue
        
    return password


if __name__ == '__main__':

    desired_length: int = 12
    use_unique_chars: bool = True
    password = generate_password(desired_password_length=desired_length,
                                 use_characters_just_once=use_unique_chars)

    print(password)