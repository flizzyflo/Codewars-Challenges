def maze_runner(maze: list, directions: list) -> str:
    
    #directions how to move within the 2D list and attached values
    dirvalue_dict= {"N": -1, "S": 1, "E": 1, "W": -1} 
    
    # try to find the starting value within the array handed over
    for idx, list in enumerate(maze):
        try:
            x, y = idx, list.index(2)
        except:
            continue
    
    # counter to control iteration
    counter = 0
    
    # alive bool for tracking status
    alive = True
    
    while alive:
        
        # main movement check with if condition
        if directions[counter] == "N" or directions[counter] == "S":
            x += dirvalue_dict[directions[counter]]
        else:
            y += dirvalue_dict[directions[counter]]
        
        # check: if moving out of bounds with directions handed over, one is dead
        if x >= len(maze) or x < 0 or y >= len(maze[0]) or y < 0:
            return "Dead"
        
        # check if one moves "into a wall"
        elif maze[x][y] == 1:
            return "Dead"
        
        # check if current position is equal to value "3" which represents the exit / finish
        elif maze[x][y] == 3:
            return "Finish"
        
        # increase while loop counter
        counter += 1
        
        # if counter equals lenght of passed in arrays and nothin else is returned, the game is lost since one is caugth within the maze
        if counter == len(directions):
            return "Lost"
          
