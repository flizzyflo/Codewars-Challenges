def dirReduc(directions: list) -> list:
    def counter_dir(first, next) -> bool:
        if (first == "NORTH" and next == "SOUTH") or (next == "NORTH" and first == "SOUTH"):
            return True
        elif (first == "WEST" and next == "EAST") or (next == "WEST" and first == "EAST"):
            return True
        else:
            return False

    first = 0
    second = 1
    while True:

        if second + 1 > len(directions):
            break

        elif counter_dir(directions[first], directions[second]):
            directions.pop(first)
            directions.pop(second - 1)
            first = 0
            second = 1

        else:
            first += 1
            second += 1

    return directions

a = ['NORTH', 'NORTH', 'WEST', 'EAST', 'SOUTH', 'EAST', 'NORTH', 'NORTH', 'WEST', 'SOUTH', 'SOUTH', 'NORTH', 'WEST', 'SOUTH', 'NORTH', 'NORTH', 'SOUTH']

print(dirReduc(a))

