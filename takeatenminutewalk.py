def is_valid_walk(walk: list) -> bool:

    result_north_south = 0
    result_east_west = 0

    if len(walk) > 10 or len(walk) < 10:
        return False

    for direction in walk:
        if direction == "n":
            result_north_south += 1
        elif direction == "s":
            result_north_south -= 1
        elif direction == "w": 
            result_east_west += 1
        elif direction == "e":
            result_east_west -= 1

    return True if result_north_south == 0 and result_east_west == 0 else False

