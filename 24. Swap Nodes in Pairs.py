class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self,head):
        previous = None
        while head:
            temporary = head.next
            head.next = previous
            previous = head

            head = temporary
        return previous
        # p,q = None,None
        # while head:
        #     p = q
        #     q = head
        #     head = head.next
        #     q.next = p
        # return p

    def swapPairs(self, head):
        if not head:
            return head
        
        if head.next is None:
            return head
        
        dummy = ListNode(next=head)
        previous = dummy
        first = head
        second = head.next

        while first and second:
            first.next = second.next
            second.next = first

            previous.next = second
            previous = first

            first = first.next
            second = first.next

        return dummy.next
    
def manualLL():
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    return root

def printLinkedList(root):
    head = root
    while head:
        print(head.val,end="->")
        head = head.next
    print("None")

result = manualLL()

s = Solution()
root = s.reverse(result)
printLinkedList(root)