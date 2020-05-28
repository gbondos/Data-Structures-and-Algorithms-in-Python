class Node:
    # constructor 
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

#create a main function to create the tree 
def spiral_traversal(root):
    if not root:
        return 
    # create two stacks
    s1 = []
    s2 = []
    s1.append(root)
    while s1 or s2:
        # check for s1 and then s2
        while s1:
            current = s1.pop()
            print(current.data, end=" ")
            if current.left:
                s2.append(current.left)
            if current.right:
                s2.append(current.right)
        # check fors2
        print(" ")
        while s2:
            current = s2.pop()
            print(current.data, end=" ")
            if current.right:
                s1.append(current.right)
            if current.left:
                s1.append(current.left)
        print(" ")

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    # etc
    spiral_traversal(root)

main()