import random

class LinkedListElement:


    def __init__(self, value: int, next: 'LinkedListElement' = None) -> None:
        self.value = value
        self.next = next


class LinkedListHead:


    def __init__(self) -> None:
        self.value = "head"
        self.next = None


    def get_list(self) -> str:

        print(self.__get_list_overview(self))

        
    def __get_list(self, 
                            LinkedListNode: 'LinkedListElement') -> None:

        if LinkedListNode.next == None:
            return f"{LinkedListNode.value} -> None"
        
        else:
            return f"{LinkedListNode.value} -> {self.__get_list(LinkedListNode.next)}"


    def is_empty(self) -> None:
        return self.next == None


    def value_in_list(self, 
                      value_to_search: int) -> bool:

        return self.__value_in_list(value_to_search, self)


    def __value_in_list(self, 
                        value_to_search: int, 
                        LinkedListNode: 'LinkedListElement') -> bool:
        
        if LinkedListNode.value == value_to_search:
            return True

        if LinkedListNode.next == None:
            return False

        return self.__value_in_list(value_to_search, LinkedListNode.next)


    def insert_new_value(self, 
                         value_to_insert: int) -> None:

        self.__insert_new_value(value_to_insert= value_to_insert, 
                                LinkedListNode= self)


    def __insert_new_value(self, 
                           value_to_insert: int, 
                           LinkedListNode: 'LinkedListElement') -> None:
        
        """Inserts elements in a sorted way, in a ascending order."""

        if LinkedListNode.next == None:
            # list is empty, no element exists.
            LinkedListNode.next = LinkedListElement(value_to_insert, None)

        elif value_to_insert <= LinkedListNode.next.value:
            # next node value is bigger than value to be inserted
            # next node has to be the predecessor of this new value and new LL element

            tempNext = LinkedListNode.next.next
            tempHead = LinkedListNode.next.value
            LinkedListNode.next.value = value_to_insert
            LinkedListNode.next.next = LinkedListElement(tempHead, tempNext)

        elif LinkedListNode.next.next == None:
            # at least one node exists, but no next element, end of list is reached.
            # create new element with the value to insert as node value.
            LinkedListNode.next.next = LinkedListElement(value_to_insert)

        else:
            self.__insert_new_value(value_to_insert, 
                                    LinkedListNode.next.next)


    def remove_value_from_list(self, 
                               value_to_remove: int) -> None:
        
        if self.is_empty() or not self.value_in_list(value_to_remove):
            return

        else:
            # Value is in list, input head node as start
            self.__remove_value_from_list(value_to_remove= value_to_remove, 
                                          LinkedListNode= self)


    def __remove_value_from_list(self, 
                                 value_to_remove: int, 
                                 LinkedListNode: 'LinkedListElement') -> None:
        
        if LinkedListNode.next.value == value_to_remove:
            LinkedListNode.next = LinkedListNode.next.next

        else:
            self.__remove_value_from_list(value_to_remove, LinkedListNode.next)



l = LinkedListHead()
l.insert_new_value(4)

for i in range(1,5):
    
    l.insert_new_value(random.randint(1, 150))


while True:
    w= input("remove elelemt (y/n)")
    if w == "y":
        e = input("element:")
        e = int(e)
        l.remove_value_from_list(e)
    
    l.get_list()
    