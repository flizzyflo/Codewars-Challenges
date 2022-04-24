
                           
def insertion_search(array: list[int]) -> list[int]:

    """Sorts an unsorted Array of integers. Setting index 0 as sorted, iterating through
    all items within the list comparing to the index 0 item. If iterated item is less, than the
    iterated item and the index 0 item switch positions, if not, the stay the same. From then on,
    index 0 and 1 are declared "sorted" and item index 2 is compared to both of them and so on and so
    forth"""

    
    for unsortedIndex in range(1, len(array)):  
        sortedIndex = unsortedIndex

        #value to be compared needs to be captured, since its an in-place operation
        #means: array[unsortedIndex] has a different value after the algorhythm is performed
        #also important to be able to switch more than one position of the same value

        arrayValue = array[unsortedIndex]

        while sortedIndex > 0:  #j gives the starting index of the 'sorted' section, for going from right to left through the sorted list.

            #if 'righttish' value is lower than 'leftish' value, they need to be switched
            if arrayValue < array[sortedIndex - 1]: 
                array[sortedIndex - 1], array[sortedIndex] = arrayValue, array[sortedIndex - 1]
    
            sortedIndex-= 1   #moving leftwards through the sorted list values

    return array


