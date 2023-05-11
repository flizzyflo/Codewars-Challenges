def increment_string(string_to_increment: str) -> str:

    """
    Increments the last number within a string if a number exists. If not, it adds a number.

    Example:
    "000008016284a29" -> "000008016284a30"
    "234tt" -> "234tt1"

    @param string_to_increment: String containing any letter or number.
    @return: Incremented string
    """

    if len(string_to_increment) == 0:
        return f"{1}"

    if not string_to_increment[len(string_to_increment) - 1].isnumeric():
        return f"{string_to_increment}{1}"

    if string_to_increment.isnumeric():
        digit_length = len(string_to_increment)
        temp_string = int(string_to_increment) + 1
        return f"{temp_string}".zfill(digit_length)

    idx_counter = len(string_to_increment) - 1
    while string_to_increment[idx_counter].isnumeric():
        idx_counter -= 1

    else:
        start_index_numbers = idx_counter + 1

    digit_length = len(string_to_increment[start_index_numbers:])

    string, numbers = string_to_increment[:start_index_numbers], int(string_to_increment[start_index_numbers:])
    numbers += 1
    string_number = str(numbers).zfill(digit_length)

    return f"{string}{string_number}"


print(increment_string("234tt"))

print(increment_string("000008016284a29"))
