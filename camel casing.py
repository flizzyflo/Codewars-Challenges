

def solution(camel_case_string: str) -> str:

    """Takes in a string as argument. Splits the string if a letter is upper case."""

    result_string: str = camel_case_string[0]

    for letter in camel_case_string[1:]:
        if letter.isupper():
            result_string += f' {letter}'
        else:
            result_string += letter

    return result_string


print(solution("TeSt"))

