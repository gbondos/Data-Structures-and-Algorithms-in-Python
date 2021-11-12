
# In this post, methods to insert a new node in linked list are discussed. A node can be added in three ways 
# 1) At the front of the linked list 
# 2) After a given node. 
# 3) At the end of the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        if self.head == "None":
            print ("The list is empty ")
            return
        current_node = self.head 
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
    
    def push(self, new_data):
        # Add a node at the front of a linked list
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self, prev_node, new_data):
        # Add a node after a given node:
        if prev_node is None:
            print("Prev node is empty")
            return 

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        # Add a node at the end
        #Create the node
        new_node = Node(new_data)

        current = self.head
        while current.next:
            current = current.next 
        current.next = new_node
        



if __name__ == '__main__':
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

    llist.printList()
    print("\n")
    llist.append(6)
    llist.push(0)
    llist.printList()
    llist.insert_after(third, "saffa")
    print("\n")
    llist.printList()