def accum(input_string: str) -> str:
    output_string = ""
    for i in range(len(input_string)):
        output_string += (input_string[i] * (i + 1) + "-")
    return output_string.title()[:-1]


print(accum("HbideVbxncC"))
