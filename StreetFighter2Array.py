
def street_fighter_selection(fighters: list[str], initial_position: tuple[int, int], moves: list[str]) -> list:
    
    fighter_result_list = []  

    x_axis_id, y_axis_id = initial_position[1],initial_position[0]  #startposition wird definitert
    for move in moves:

        if move =="up":
            y_axis_id=0
            fighter_result_list.append(fighters[y_axis_id][x_axis_id])

        elif move == "down":
            y_axis_id=1
            fighter_result_list.append(fighters[y_axis_id][x_axis_id])

        elif move == "right":
            x_axis_id += 1
            if x_axis_id > len(fighters[0])-1:
                x_axis_id = 0
                fighter_result_list.append(fighters[y_axis_id][x_axis_id])

            else:
                fighter_result_list.append(fighters[y_axis_id][x_axis_id])

        elif move == "left":
            x_axis_id -= 1
            if x_axis_id < 0:
                x_axis_id = len(fighters[0]) - 1
                fighter_result_list.append(fighters[y_axis_id][x_axis_id])

            else:
                fighter_result_list.append(fighters[y_axis_id][x_axis_id])
                
    return fighter_result_list

## Example input for testing purposes

## print(street_fighter_selection([["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
##                                 ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]],(0,0),['left', 'right', 'down', 'left']))