from unittest import result


def rank(st: str, we: int, n:int) -> int:
    
    if st=="":
        return "No participants"

    name_values, letter_values, i, alphabet = dict(), dict(), 1, "abcdefghijklmnopqrstuvwxyz"

    # Creation of letter values of alphabetic letters
    for letter in alphabet:
        letter_values[letter] = i
        i += 1

    st = st.split(",")
    
    if n > len(st):
        return "Not enough participants"
    
    # Evaluation of students names
    for student in st:
        name_values[student] = len(student)
        for letter in student:
            name_values[student] += int(letter_values[letter.lower()])

    # Calculation of weights 
    for index, weight in enumerate(we):
        name_values[st[index]] *= weight

    # Output of n´th student

    result_list = sorted(name_values, key=name_values.get, reverse=True)
    
    temp_result = []

    for key, value in name_values.items():
        if value == name_values[result_list[n- 1]] and key not in temp_result:
            temp_result.append(key)
        


    temp_result.sort()
    return temp_result[0]

print(rank(st='William,Willaim,Olivia,Olivai,Lily,Lyli',we=[1, 1, 1, 1, 1, 1],n=1))
