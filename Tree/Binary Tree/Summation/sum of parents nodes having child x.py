class Node:
    # constructor 
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

#create a main function to create the tree 

def parent_nodes_with_child_x(root, x, total):
    if not root:
        return total[0]
    
    if (root.left and root.left.data == x) or (root.right and root.right.data == x):
        total[0] += root.data
    parent_nodes_with_child_x(root.left, x, total)
    parent_nodes_with_child_x(root.right, x, total)
    

def main():
    root = Node(4)              #      4      
    root.left = Node(2)         #     / \      
    root.right = Node(5)         #   2   5      
    root.left.left = Node(7)     #  / \ / \      
    root.left.right = Node(2) #    7  2 2 3  
    root.right.left = Node(2)  
    root.right.right = Node(3)  
      
    x = 2
    total = [0]
    parent_nodes_with_child_x(root, x, total)
    print(" Total is ", total[0])

    

main()