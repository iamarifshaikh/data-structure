from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def inorder(self,root):
        current = root
        print(current,root)
        stack = []
        result = []

        while current or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                popped = stack.pop()
                result.append(popped.val)
                current = popped.right
        return result

root = TreeNode(1)

root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)

s = Solution()
print(s.inorder(root))