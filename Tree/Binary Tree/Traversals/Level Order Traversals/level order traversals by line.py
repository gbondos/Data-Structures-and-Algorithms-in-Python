class Node:
    # constructor 
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None

def lvl_by_line(root):
    if not root:
        return 
    q = []
    q.append(root)
    count = 0
    while q:
        count = len(q)
        while count:
            current = q.pop(0)
            print(current.data, end=" ")
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            count -= 1
        print(" ")

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # etc
    lvl_by_line(root)
main()