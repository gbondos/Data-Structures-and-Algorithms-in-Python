class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def printCurrentLevel(root, level):
    if not root:
        return 
    if level == 1:
        print(root.data, end= " ")
    elif level > 1:
        printCurrentLevel(root.left, level -1)
        printCurrentLevel(root.right, level -1)


def height(root):
    if not root:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
def LevelOrder(root):
    h = height(root)
    for level in range(1, h):
        printCurrentLevel(root, level)
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

    inorder(root)

    print("Heigh of tree is ", height(root))
    print("Level Order Traversal")
    LevelOrder(root)

main()
