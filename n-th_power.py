
def index(array: list[int], n: int) -> int:
    
    if n >= len(array):
        return -1

    else:
        return array[n] ** n