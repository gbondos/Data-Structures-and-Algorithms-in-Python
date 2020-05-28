#print a given tree using level order traversals

def level(root):
    if root is None:
        return 
    q = []
    q.append(root)
    while q:
        current = q.pop(0)
        print(current.data, end=" ")
        if current.left:
            q.append(current.left)
             
        if current.right:
            q.append(current.right)
     
print("hie")