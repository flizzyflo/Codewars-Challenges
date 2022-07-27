

def move_numbers(array: list, number: int = 0) -> list:

    if array == []:
        return []

    number_to_move = number

    sorted = False

    total_numbers = array.count(0)

    while sorted == False:  

        for index, number in enumerate(array):
            if number == number_to_move and (index + 1) < len(array):
                temp = array[index + 1]
                array[index] = temp
                array[index + 1] = number

            if sum(array[len(array) - total_numbers:]) == total_numbers * number_to_move:
                sorted = True


    return array

