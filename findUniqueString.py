def find_uniq(arr: list[str]) -> str:
    """Function will return the unique string out of an array containing strings. 
    Returns the unique string out of an array containing similar strings except one."""
    
    # looping through part of the string array.
    for idx, string in enumerate(arr[1:], 2):
        
        # break condition of for loop to not run out of bounds
        if idx > len(arr) - 1:
            break
        
        # create sets containing the single letters
        startString =set(arr[idx - 2].lower())  # idx - 2
        middleString = set(string.lower())      # idx - 1
        LastString = set(arr[idx].lower())      # idx 
        
        # if sets equal each other, the unique string is not found yet
        if sorted(startString) == sorted(middleString) == sorted(LastString):
            continue
      
        #first string in current comparison iteration is unique string
        elif sorted(startString) != sorted(middleString) == sorted(LastString):
            return arr[idx - 2]
        
        # second string in current comparison iteration is unique string
        elif sorted(startString) != sorted(middleString) != sorted(LastString):
            return arr[idx - 1]
        
        # third string in current comparison iteration is unique string
        elif sorted(startString) == sorted(middleString) != sorted(LastString):
            return arr[idx]
