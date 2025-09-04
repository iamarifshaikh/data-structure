from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_manual_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    
    
root = create_manual_tree()
level_order(root)