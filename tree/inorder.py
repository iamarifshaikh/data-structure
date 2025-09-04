class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_manual_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(8)
    return root

def inorderTraversal(root):
    stack = []
    current = root
    result = []

    while current is not None or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.data)

        current = current.right

    return result

root = create_manual_tree()
result = inorderTraversal(root)
print(result)