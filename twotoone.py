def longest(a1: str, a2: str) -> str:
    result_string = a1 + a2
    result_string = list(set(result_string))
    result_string.sort()

    return "".join(result_string)


    


print(longest("abcde", "def"))