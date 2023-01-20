
class Node(object):
    def __init__(self, data, next= None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:

        if self.data == None:
            return "None"
        
        return f"{self.data} -> {self.next}"

def append(listA: Node, listB: Node):
    
    if not listB:
        return listA
    
    if not listA:
        return listB
    
    cur_node = listA
    
    while cur_node.next:
        cur_node = cur_node.next

    cur_node.next = listB
    return listA


a = Node(1, Node(2, Node(5)))
b = Node(3, Node(21, Node(25)))
print(a)
print(append(a, b))