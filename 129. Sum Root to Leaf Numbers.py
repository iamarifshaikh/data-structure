class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self,root) -> int:
        result = []
        def recursion(root,num):
            if root.left == None and root.right == None:
                num += str(root.val)
                result.append(int(num))
                return
            
            num += str(root.val)
            recursion(root.left,num)
            recursion(root.right,num)

        recursion(root,"")
        return sum(result)
    
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(8)

s = Solution()
result = s.sumNumbers(root)
print(result)