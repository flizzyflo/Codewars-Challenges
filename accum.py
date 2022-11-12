<<<<<<< HEAD

=======
>>>>>>> 5c6661fc068a1bb5e06b9286fa4341b523be25c9
def accum(input_string: str) -> str:
    output_string = ""
    for i in range(len(input_string)):
        output_string += (input_string[i] * (i + 1) + "-")
    return output_string.title()[:-1]


print(accum("HbideVbxncC"))
