class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        curr = head
        count = 1

        while count != left -1:
            curr = curr.next
            count += 1
        
        prev = curr.next
        previous = None

        while count != right:
            temporary = prev.next
            prev.next = previous
            previous = prev

            prev = temporary
            count += 1
            
        curr.next = previous
        return head
    
    def convertArrayToLL(self,head):
        root = ListNode(head[0])
        newList = root
        for i in range(1,len(head)):
            new_node = ListNode(head[i])
            newList.next = new_node
            newList = newList.next
        
        return root
    
    def printLinkedList(self,head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")

s = Solution()
head = s.convertArrayToLL([1,2,3,4,5])
rl = s.reverseBetween(head,2,4)
s.printLinkedList(rl)