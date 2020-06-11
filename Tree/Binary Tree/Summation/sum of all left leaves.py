class Node:
    # constructor 
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

#create a main function to create the tree 

def leftLeaves(root, total):
    if not root:
        return 0
    if root.left:
        if root.left is None and root.right is None:
            total[0] += root.data 
    leftLeaves(root.left, total)
    leftLeaves(root.right, total)

def sum_of_all_leftLeaves(root):
    total = [0]
    leftLeaves(root.left, total)
    leftLeaves(root.right, total)
    return total[0]
    

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
    
    total = sum_of_all_leftLeaves(root)
    print(" Total is ", total)

    

main()