

def move_numbers(array: list, number: int = 0) -> list:

    if not array:
        return []

    number_to_move: int = number
    sorted: bool = False
    total_numbers: list[int] = array.count(0)

    while not sorted:  

        for index, number in enumerate(array):
            if number == number_to_move and (index + 1) < len(array):
                temp = array[index + 1]
                array[index] = temp
                array[index + 1] = number

            if sum(array[len(array) - total_numbers:]) == total_numbers * number_to_move:
                sorted = True


    return array

