class Node:
    # constructor 
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

#create a main function to create the tree 
def reverse_level(root):
    s = []
    q = []
    q.append(root)
    while q:
        current = q.pop(0)
        s.append(current) 
        if current.right:
            q.append(current.right)
        if current.left:
            q.append(current.left)
    
    while s: 
        current = s.pop()
        print(current.data, end=" ")



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

    reverse_level(root)

main()