def dirReduc(directions: list) -> list:
    
    def counter_dir(first, next) -> bool:
        if (first == "NORTH" and next == "SOUTH") or (first == "SOUTH" and next == "NORTH" ):
            return True
        elif (first == "WEST" and next == "EAST") or (first == "EAST" and next == "WEST"):
            return True
        else:
            return False
    
    result_directions = []
    id = 1
    for direction in directions:
        
        if id >= len(directions):
            break
            
        elif counter_dir(direction, directions[id]):
            id += 1
            continue
        
        else:
            id += 1
            result_directions.append(direction)
        
    return result_directions


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))