class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def traverse(root):
    if root is None:
        return

    q = []
    q.append(root)
    
    while (len(q) > 0):
        temp = q.pop(0)
        print(temp.data)

        if temp.left is not None:
            q.append(temp.left)

        if temp.right is not None:
            q.append(temp.right)

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(5)
tree.left.right = Node(4)

traverse(tree)
