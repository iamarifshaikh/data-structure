from collections import deque,Counter
from math import inf

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution: 
    def zigzagLevelOrder(self,root):
        level = []
        queue = deque([root])
        zigzag = False

        while queue:
            stack = []
            for _ in range(len(queue)):
                if zigzag: 
                    popped = queue.pop()
                    stack.append(popped.val)

                    if popped.right: queue.appendleft(popped.right)
                    if popped.left: queue.appendleft(popped.left)
                    
                else: 
                    popped = queue.popleft()
                    stack.append(popped.val)

                    if popped.left: queue.append(popped.left)
                    if popped.right: queue.append(popped.right)
            
            zigzag = not zigzag
            level.append(stack)

        return level
        
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
    
    def isBalanced(self, root):
        if not root:
            return True

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if abs(left_height - right_height) > 1:
            return False

        left_h = self.isBalanced(root.left)
        right_h = self.isBalanced(root.right)

        return left_h and right_h

    def getHeight(self,root):
        if not root:
            return 0
        
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        return 1 + max(left, right)
    
    def is_symmetric(self, root):
        q = deque([root])
        
        while q:
            left_stack = []
            right_stack = []

            for i in range(len(q)):
                popped = q.popleft()
                
                if popped.left:
                    q.append(popped.left)
                    left_stack.append(popped.left.val)
                else: left_stack.append(None)

                if popped.right:
                    q.append(popped.right)
                    right_stack.append(popped.right.val)
                else: right_stack.append(None)


            if (left_stack and not right_stack) or (not left_stack and right_stack): return False
            
            if len(left_stack) != len(right_stack):return False
            
            if left_stack != right_stack[::-1]:return False
            
        return True
    # def isSymmetric(self, root):
    #     if not root:
    #         return True

    #     q = deque([root])

    #     while q:
    #         level = []
    #         for _ in range(len(q)):
    #             popped = q.popleft()

    #             if popped:
    #                 level.append(popped.val)
    #                 q.append(popped.left)
    #                 q.append(popped.right)
    #             else:
    #                 level.append(None)

    #         if level != level[::-1]:
    #             return False

    #     return True

    def invertTree(self,root):
        if not root: return []
        q = deque([root])
        stack = []

        while q:
            for _ in range(len(q)):
                popped = q.popleft()
                stack.append(popped.val)

                if popped.right:
                    q.append(popped.right)
                
                if popped.left:
                    q.append(popped.left)
        return stack
    
    def removeLeafNodes(self,root,target):
        if root is None:
            return 

        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)
        
        if root.val == target and root.left is None and root.right is None:
            return None

        return root
    
    def findBottomLeftValue(self, root):
        queue = deque([root])
        bottom_node = root.val

        while queue:
            bottom_left = False

            for _ in range(len(queue)):
                popped = queue.popleft()
                    
                if popped.left: 
                    queue.append(popped.left)
                else:
                    bottom_left = True
                    bottom_node = popped.val
                    print(bottom_node,bottom_left)

                if popped.right: 
                    queue.append(popped.right)
                else:
                    if not bottom_left: 
                        bottom_node = popped.val
                        print(bottom_node,bottom_left)
        
        return bottom_node


        bfs()
        # bottom_node = root.val
        # maxlevel = 0 
    
        # def dfs(root,level):
        #     if not root:
        #         return
            
        #     if maxlevel < level:
        #         maxlevel = level
        #         bottom_node = root.val

        #     dfs(root.left,level + 1)
        #     dfs(root.right,level + 1)
        
        # dfs(root,0)
        # return bottom_node

    def allRootToLeaf(self, root):
        all_path = []

        def dfs(root,path):
            if not root: return
            path.append(root.val)
            print(root.val,path)
            
            if root.left is None and root.right is None:
                all_path.append(path[:])
                return

            dfs(root.left,path)
            path.pop()
            print(path,root.val)
            dfs(root.right,path)
            path.pop()

        dfs(root,[])
        return all_path

    def findSubtrees(self,root):
        result = []
        def dfs():
            if root is None:
                return []
            
            current = []


            left_tree = self.recursion(root.left)
            right_tree = self.recursion(root.right)
            
            current = [root.val] + left_tree + right_tree

            result.append(current)
            return current

        dfs(root)
        return result

    def maximum(self,root):
        maxi = [float("-inf")]

        def maxPath(root):
            if not root: return 0
            
            left_sum = max(maxPath(root.left),0)
            right_sum = max(maxPath(root.right),0)

            curr_sum = left_sum + right_sum + root.val

            maxi[0] = max(maxi[0],curr_sum) 

            return max(left_sum + root.val,right_sum + root.val)

        maxPath(root)
        return maxi[0]

    def pathSum2(self, root, targetSum):
        result = []
        
        def recursion(root,path):
            if root is None: return
            if root.left is None and root.right is None:
                path.append(root.val)
                if targetSum == sum(path):
                    result.append(path.copy())
                return

            path.append(root.val)

            recursion(root.left,path)
            path.pop()
            recursion(root.right,path)

        recursion(root.left,[root.val])
        recursion(root.right,[root.val])

        return result
    
    def pathSum3(self, root, targetSum):
        pass
        
    def binaryTreePaths(self, root):
        result = []
        def recursion(root,path):
            if not root: 
                return
            
            if root.left is None and root.right is None:
                path = path + f"->{root.val}"
                result.append(path)
                return 
            
            path = path + f"->{root.val}"
            
            recursion(root.left,path)
            recursion(root.right,path)


        recursion(root.left,f"{root.val}")
        recursion(root.right,f"{root.val}")
        return result
    
    def smallestFromLeaf(self, root):
        pass

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
root = build_tree([1,2,3,None,5])
print(s.binaryTreePaths(root))
