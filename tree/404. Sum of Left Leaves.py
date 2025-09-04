class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    isLeft = True
    sumOfleft = 0
    def sumOfLeftLeaves(self, root) -> int:
        if root.left == None and root.right == None and self.isLeft:
            self.sumOfleft += root.val
            return self.sumOfleft

        if root == None:
            return self.umOfleft

        result = self.sumOfLeftLeaves(root.left)
        self.isLeft = False
        self.sumOfLeftLeaves(root.right)
        return result

def create_manual_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root

root = create_manual_tree()
s = Solution()
result = s.sumOfLeftLeaves(root)
print(result)