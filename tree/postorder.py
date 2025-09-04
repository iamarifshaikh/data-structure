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

def postorder(root):
    result = []
    stack  = []
    current = root

    while current is not None or stack:
        while current:
            current = current.left

    # if root == None:
    #     return None
    
    # postorder(root.left)
    # postorder(root.right)
    # print(root.data,end="->")
    return result
root = create_manual_tree()
postorder(root)