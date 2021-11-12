
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second     = Node(2)
    third      = Node(3)
    fourth     = Node(4)
    fifth      = Node(5)

    llist.head.next = second
    second.next = third
    third.next  = fourth
    fourth.next = fifth 

    