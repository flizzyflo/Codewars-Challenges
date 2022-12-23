

def solution(camel_case_string: str) -> str:

    result_string: str = camel_case_string[0]
    for letter in camel_case_string[1:]:
        if letter.isupper():
            result_string += f' {letter}'
        else:
            result_string += letter

    return result_string

