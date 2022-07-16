
                           
def insertion_sort(array: list[int]) -> list[int]:

    """Sorts an unsorted Array of integers. Setting index 0 as sorted, iterating through
    all items within the list comparing to the index 0 item. If iterated item is less, than the
    iterated item and the index 0 item switch positions, if not, the stay the same. From then on,
    index 0 and 1 are declared "sorted" and item index 2 is compared to both of them and so on and so
    forth"""

    
    for unsortedIndex in range(1, len(array)):  
        sortedIndex = unsortedIndex

        arrayValue = array[unsortedIndex]

        while sortedIndex > 0:  #j captures the most right index of the 'sorted' area of the array, for going from right to left through the sorted list for comparing it to the unsorted values.

            #if 'unsorted' value is lower than 'sorted' value, they need to be switched to keep the sort-by-value order
            if arrayValue < array[sortedIndex - 1]: 
                array[sortedIndex - 1], array[sortedIndex] = arrayValue, array[sortedIndex - 1]
    
            sortedIndex-= 1   #moving leftwards through the sorted list values

    return array  #return the sorted array


