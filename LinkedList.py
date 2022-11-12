
class LinkedListElement:

    """List Element Class to represent the value and reference the next element within the linked list."""

    def __init__(self, value: int, next: 'LinkedListElement' = None) -> None:
        self.value = value
        self.next = next


class LinkedListHead:

    """Linked List Control Class. Manages the linked list and accesses the elements. Is used to create, insert and remove elements from the list.
    Is also used to represent the list."""

    def __init__(self) -> None:
        self.value = "head"
        self.next = None


    def get_list(self) -> str:

        """Method to represent the list as printed statement"""

        print(self.__get_list(self))

        
    def __get_list(self, LinkedListNode: 'LinkedListElement') -> None:

        """Private Method to print the list elements."""

        if LinkedListNode.next == None:
            return f"{LinkedListNode.value} -> None"
        
        else:
            return f"{LinkedListNode.value} -> {self.__get_list(LinkedListNode.next)}"


    def is_empty(self) -> bool:
        
        """Returns the boolean value if the list contains elements or not"""

        return self.next == None


    def value_in_list(self, value_to_search: int) -> bool:

        """Returns a boolean value if a specific value is within the list or not"""

        return self.__value_in_list(value_to_search, self)


    def __value_in_list(self, value_to_search: int, LinkedListNode: 'LinkedListElement') -> bool:
        
        """Private method which is used to look up values within the linked list. Returns a boolean value according to the existence or absence of a specific value."""

        if LinkedListNode.value == value_to_search:
            return True

        if LinkedListNode.next == None:
            return False

        return self.__value_in_list(value_to_search, LinkedListNode.next)


    def insert_new_value(self, value_to_insert: int) -> None:

        """Public Method to insert a new value into the linked list."""

        self.__insert_new_value(value_to_insert= value_to_insert, LinkedListNode= self)


    def __insert_new_value(self, value_to_insert: int, LinkedListNode: 'LinkedListElement') -> None:
        
        """Private Method to insert elements in a sorted way, in a ascending order."""

        if LinkedListNode.next == None:
            # list is empty, no element exists.
            LinkedListNode.next = LinkedListElement(value_to_insert, None)

        elif value_to_insert < LinkedListNode.next.value:
            # next node value is bigger than value to be inserted
            # next node has to be the predecessor of this new value and new LL element

            tempNext = LinkedListNode.next
            LinkedListNode.next = LinkedListElement(value_to_insert, tempNext)


        elif LinkedListNode.next.next == None:
            # at least one node exists, but no next element, end of list is reached.
            # create new element with the value to insert as node value.
            LinkedListNode.next.next = LinkedListElement(value_to_insert)

        else:
            self.__insert_new_value(value_to_insert, LinkedListNode.next)


    def remove_value_from_list(self, value_to_remove: int) -> None:
        
        """Removes an element from the linked list"""

        if self.is_empty() or not self.value_in_list(value_to_remove):
            return

        else:
            # Value is in list, input head node as start
            self.__remove_value_from_list(value_to_remove= value_to_remove, 
                                          LinkedListNode= self)


    def __remove_value_from_list(self, value_to_remove: int, LinkedListNode: 'LinkedListElement') -> None:
        
        """Private method to remove a specific value from the linked list."""

        if LinkedListNode.next.value == value_to_remove:
            LinkedListNode.next = LinkedListNode.next.next

        else:
            self.__remove_value_from_list(value_to_remove, LinkedListNode.next)


    def is_sorted(self) -> bool:
        
        """Checks whether the linked list elements are sorted or not."""

        return self.__is_sorted(self)

    
    def __is_sorted(self, LinkedListNode: 'LinkedListElement') -> bool:

        """Private method to return a boolean if the list is sorted or not."""

        if LinkedListNode.next == None:
            return True
        
        elif not isinstance(LinkedListNode.value, int):
            return self.__is_sorted(LinkedListNode.next)

        elif LinkedListNode.value > LinkedListNode.next.value:
            return False

        else:
            return self.__is_sorted(LinkedListNode.next)


    def sort_elements(self) -> None:
        
        """Main sort function. applies some sort ob bubblesort to sort the linked list. Sorts as long as the is_sorted() returns true."""

        while True:
            self.__sort_elements(self)
            
            if self.is_sorted():
                break

    def __sort_elements(self, LinkedListNode: 'LinkedListElement') -> None:
        
        """Private Method to sort the linked list elements"""

        # starts with head node. next pointer points to first linked list element
        if LinkedListNode.next == None or LinkedListNode.next.next == None:
            return
        
        # start -> 8 -> 4 -> 6
        elif LinkedListNode.next.next.value < LinkedListNode.next.value:
   
            tempNextNext = LinkedListNode.next.next # 4
            tempNext = LinkedListNode.next # 8
            tempNext.next = tempNextNext.next # 6
            tempNextNext.next = tempNext
            LinkedListNode.next = tempNextNext

        else:
            return self.__sort_elements(LinkedListNode.next)

