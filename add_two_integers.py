
def add_integer(array: list[int], target_number: int) -> tuple[int]:

    #stores number, index pair
    storage: dict[int, int] = { }

    for index, current_number in enumerate(array):
        desired_number = target_number - current_number

        if desired_number in storage.keys():
            return (index, storage[desired_number])
        
        storage[current_number] = index

    raise IOError("Target number can not be calculated")


