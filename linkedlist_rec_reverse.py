class Node(object):
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        
        if self.data == None:
            return "None"

        return f"{self.data} -> {self.next}"
    

def reverse(head: Node, former_head: Node = None):
    
    """3 -> 5 -> 7 -> None"""

    # reached end of the list
    if head.next == None:
        # head data is last element which is not None
        # former head is Node element of former element

        # 7 -> 5 -> 7
        return Node(head.data, former_head)

    return reverse(head.next, head)

c= Node(3, Node(5, Node(7)))
c = reverse(c)
print(c)