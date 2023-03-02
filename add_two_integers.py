
def add_integer(array: list[int], target_number: int) -> tuple[int]:
    """
    Checks if the target number can be calculated from two numbers stored within the array.
    If yes, returns a tuple containing the index position and the desired number.

    @param array: Array containing integers to be summed up
    @param target_number: Desired number which should be checked if its calculatable.
    @return: Tuple of index position within the array and the number at indexposition.
    """
    #stores number, index pair
    storage: dict[int, int] = { }

    for index, current_number in enumerate(array):
        desired_number = target_number - current_number

        if desired_number in storage.keys():
            return (index, storage[desired_number])
        
        storage[current_number] = index

    raise IOError("Target number can not be calculated")


