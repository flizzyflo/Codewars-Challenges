def encrypt_this(text: str) -> str:
    
    if len(text) == 0:
        return ""

    strings: list[str] = text.split()
    solution: list[str] = list()
    res: str = ""

    for string in strings:
        if len(string) == 1:
            res = str(ord(string))
        else:
            for index, letter in enumerate(string):
                
                second_letter: str = string[1]
                last_letter: str = string[-1]

                if index == 0:
                    res += str(ord(letter))
                
                elif index == 1:
                    res += last_letter

                elif index == len(string) -1:
                    res += second_letter

                else:
                    res += string[index]
            
        solution.append(res)
        res = ""

    return " ".join(solution)


print(encrypt_this("hello world"))
