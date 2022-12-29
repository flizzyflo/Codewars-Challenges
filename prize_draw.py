
import string
string.punctuation
def rank(students: str, weights: int, rank:int) -> int:
    
    students = students.split(",")

    if students=="":
        return "No participants"

    if rank > len(students):
        return "Not enough participants"
    
    alphabet = string.ascii_lowercase
    letter_values: dict[str, int] = {letter: value for value, letter in enumerate(alphabet, 1)}
    rank: int = rank - 1

    # Calculation of weighted student name values
    weighted_name_values: dict[str, int] = {student: evaluate_student_name(student, letter_values) * weights[index] for index, student in enumerate(students, 0)}
    sorted_students = sorted(weighted_name_values, reverse= True, key= weighted_name_values.get)
    desired_student = sorted_students[rank]
    current_solution: list[str] = [desired_student]
    desired_student_name_value: int = weighted_name_values[desired_student]

    for student in sorted_students:
        if weighted_name_values[student] == desired_student_name_value and student not in current_solution:
            current_solution.append(student)
    return current_solution[0]


def evaluate_student_name(student: str, letter_values: dict[str, int]) -> int:

    return sum(letter_values[letter.lower()] for letter in student) + len(student)

print(rank('William,Willaim,Olivia,Olivai,Lily,Lyli', [1, 1, 1, 1, 1, 1], 1))
