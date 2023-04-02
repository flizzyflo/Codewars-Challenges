def expanded_form(number: int) -> str:
    if number < 10:
        return str(number)

    stringified_number = str(number)
    extracted_number = stringified_number[0] + (len(stringified_number) - 1) * "0"
    rest = number % int(extracted_number)

    if rest == 0:
        return extracted_number

    return f"{extracted_number} + {expanded_form(number=rest)}"