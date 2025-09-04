class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        if not head:
            return head

        while head and head.val == target:
            head = head.next
        
        if not head: return None
        
        head.prev = None
        
        back = head
        front = head.next

        while front:
            if front.val == target:
                back.next = front.next
                if front.next: front.next.prev = back
            else:back = front
            front = front.next
        
        return head
    
    def sortList(self, head):
        pass

    def removeDuplicates(self,head):
        if not head or not head.next:
            return head

        first = head
        second = head.next

        while first and first.next:
            if first.val == second.val:
                while first.val == second.val:
                    if not second.next:
                        break
                    second = second.next
                
                if first.val != second.val:
                    first.next = second
                    second.prev = first
                else:
                    first.next = None


            if first.next: first = first.next
            else: break
            
            if second.next: second = second.next
            else: break

        return head

    def deleteKthElement(self, head, k):
        if head is None:
            return None
        
        if k == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None            
            return new_head
        
        count = 1
        KNode = head

        while KNode and count < k:
            KNode = KNode.next
            count += 1

        if KNode is None: return head

        if KNode.next:
            KNode.next.prev = KNode.prev
        
        if KNode.prev:
            KNode.prev.next = KNode.next
        
        return head
     
    def deleteTail(self, head):
        curr = head
        while curr.next.next:
            curr = curr.next
        self.printDLL(curr)
        curr.next = None
        return head
     
    def convertArrayToDLL(self,array):
        head = ListNode(array[0])
        previous = head

        for i in range(1,len(array)):
            temp = ListNode(array[i],None,previous)
            previous.next = temp
            previous = temp
        return head
    
    def deleteHeadOfDLL(self,head):
        new_head = head.next
        new_head.prev = None
        head.next = None
        return new_head
    
    def tailOfDLL():
        pass

    def printDLL(self,head):
        while head:
            print(head.val, end="->")
            head = head.next
        print()
        

s = Solution()
head = s.convertArrayToDLL([7,7,7,7])    
# new_dll = s.removeDuplicates(head)
new_list = s.deleteAllOccurrences(head,7)
s.printDLL(new_list)
# new_head = s.deleteKthElement(head,3)
# s.sortList()