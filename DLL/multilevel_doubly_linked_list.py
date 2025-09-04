class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        current = head

        while current:
        
            if current.child:
                child_nodes = self.flatten(current.child)
                
                current.child = None
                child_nodes.prev = current 
                
                next_nodes = current.next
                
                current.next = child_nodes
                
                add = child_nodes
                while add.next:
                    add = add.next

                if next_nodes: 
                    next_nodes.prev = add
                    add.next = next_nodes

            current = current.next

        return head
    
    def printDLL(self,head):
        while head:
            print(head.val, end="->")
            head = head.next
        print()
    
    def ManualTree(self):
        root = Node(1)
        root.child = Node(2)
        root.child.child = Node(3)
        # root.next = Node(2, prev=root)
        # root.next.next = Node(3, prev=root.next)
        # root.next.next.next = Node(4, prev=root.next.next)
        # root.next.next.next.next = Node(5, prev=root.next.next.next)
        # root.next.next.next.next.next = Node(6, prev=root.next.next.next.next)

        # # child of 3 → 7
        # root.next.next.child = Node(7)
        # root.next.next.child.next = Node(8, prev=root.next.next.child)
        # root.next.next.child.next.next = Node(9, prev=root.next.next.child.next)
        # root.next.next.child.next.next.next = Node(10, prev=root.next.next.child.next.next)

        # # child of 8 → 11
        # root.next.next.child.next.child = Node(11)
        # root.next.next.child.next.child.next = Node(12, prev=root.next.next.child.next.child)

        return root
    
s = Solution()
head = s.ManualTree()
flatten = s.flatten(head)
s.printDLL(flatten)