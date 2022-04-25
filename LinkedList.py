

class LinkedList:

    def __init__(self, nodeValue: int, next: object = None) -> None:
        self.head = nodeValue
        self.next = next

    def __str__(self) -> None:
        return f"{self.head} -> {self.next}"


    def searchValue(self, valueToSearch: int, LinkedListObject: object) -> bool:
        
        if LinkedListObject.head == valueToSearch:
            return True

        if LinkedListObject.next == None:
            return False

        return self.searchValue(valueToSearch, LinkedListObject.next)


    def insertValue(self, valueToInsert: int, ListObject: object) -> None:
        
        if ListObject.next == None:
            ListObject.next = LinkedList(valueToInsert)

        elif valueToInsert < ListObject.head:
            tempNext = ListObject.next
            tempHead = ListObject.head
            ListObject.head = valueToInsert
            ListObject.next = LinkedList(tempHead, tempNext)
        
        else:
            self.insertValue(valueToInsert, ListObject.next)


    def sortValues(self, ListObject: object) -> None:
        pass

        
    def removeValue(self, valueToRemove: int, ListObject: object) -> None:
        
        if not self.searchValue(valueToRemove, ListObject):
            return "Value not found in List"

        if ListObject.next == None:
            return "Value not found in List" 

        if ListObject.next.head == valueToRemove:
            tempNext = ListObject.next.next
            del ListObject.next 
            ListObject.next = tempNext
            return "Value removed"

        else:
            self.removeValue(valueToRemove, ListObject.next)







