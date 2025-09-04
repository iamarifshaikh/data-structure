from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        def recursion(root,count):
            if not root: return count
            count += 1
            
            max_count = max(recursion(root.left,count),recursion(root.right,count))
            return max_count
        return recursion(root,0) 

    def inorder(self,root):
        stack = []
        result = []

        while root or stack:
            print(root)
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                popped = stack.pop()
                result.append(popped.val)
                root = popped.right
        return result

    # def preorder(self,root):
    #     stack = []
    #     result = []

    #     while root or stack:
    #         if root is not None:
    #             stack.append(root)
    #             result.append(root.val)
    #             root = root.left
    #         else:
    #             popped = stack.pop()
    #             root = popped.right
    #     return result
    
    def preorder(self,root):
        preorder = []

        if root is None: return preorder

        stack = []
        stack.append(root)

        while stack:
            popped = stack.pop()
            preorder.append(popped.val)
            if popped.right: stack.append(popped.right)
            if popped.left: stack.append(popped.left)
        return preorder
    
    def postorder(self,root):
        postorder = []
        if root is None: return postorder

        stack = []
        stack.append(root)

        while stack:
            print(root.val)
            popped = stack.pop()
            postorder.append(popped.val)

            if popped.left: stack.append(popped.left)
            if popped.right: stack.append(popped.right)

        postorder.reverse()
        return postorder
    def bfs(self,root):
        q = deque([root])
        
        stack = []

        while q:
            length = len(q)
            result = [] 
    
            for _ in range(length):
                pop = q.popleft()        
                result.append(pop.val)

                if pop.left is not None:
                    q.append(pop.left)
                
                if pop.right is not None:
                    q.append(pop.right)
            stack.append(result)
        return stack
    
def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root
    
s = Solution()
root = build_tree( [3, 9, 20, None, None, None , 7])
print(s.maxDepth(root))