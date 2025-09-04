class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p,q) -> bool:
        if p == None and q == None:
            return True
        
        if (p != None and q == None) or (p == None and q!= None) or not(p.val == q.val):
            return False

        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
        return left and right

def create_manual_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    return root

def create_manual_tree_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    return root

p = create_manual_tree()
q = create_manual_tree_2()

s = Solution()
result = s.isSameTree(p,q)
print(result)