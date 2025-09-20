class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        h1 = ListNode()
        h2 = ListNode()
        small = h1
        great = h2
        curr = head
        
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                great.next = curr
                great = great.next
            curr = curr.next
        great.next = None
        small.next = h2.next
        return h1.next
        # h1 = ListNode()
        # small = h1
        # curr = head
        # previous = None
        
        # while curr and curr.val < x:
        #     temporary = curr.next
        #     small.next = curr
        #     small = small.next
        #     curr = temporary

        # # self.printLinkedList()

        # while curr:
        #     if curr.val < x:
        #         if curr and curr.next:
        #             previous.next = curr.next           
        #             small.next = curr
        #             small = small.next
        #             previous = previous.next
        #         else:
        #             small.next = curr
        #             small = small.next
        #             previous.next = None
        #         if previous and previous.next:
        #             curr = previous.next
        #         else:
        #             small.next = head
        #             return h1.next
        #     else:
        #         previous = curr
        #         if curr and curr.next:
        #             curr = curr.next

        # small.next = head
        # return h1.next
    
    def mergeNodes(self, head):
        pass
        
    def isPalindrome(self, head):
        pass
    
    def addTwoNumbers2(self, l1, l2):
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        previous = None
        total = stack1.pop() + stack2.pop()
        head = ListNode(total % 10)
        head.next = previous
        previous = head
        carry = total // 10

        while stack1 or stack2 or carry:
            h1 = stack1.pop() if stack1 else 0
            h2 = stack2.pop() if stack2 else 0

            total = h1 + h2 + carry
            carry = total // 10
            node = ListNode(total % 10)
            node.next = previous
            previous = node
    
        return previous

    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        previous = head
        current = head.next.next

        while current and current.next:
            self.printLinkedList(previous)
            self.printLinkedList(current)
            previous = previous.next
            current = current.next.next

        previous.next = previous.next.next
        return head
    
    def swapPairs(self,head):
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head

        first = head
        second = head.next
        previous = dummy

        while first and first.next:
            temporary = second.next
            
            first.next = temporary
            second.next = first
            previous.next = second

            first = temporary
            previous = second.next
            if first:
                second = first.next 

        return dummy.next
    
    def reverseBetween(self, head, left, right):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0,next=head)
        previous = head

        for _ in range(left - 1):
            previous = previous.next
        self.printLinkedList(previous.next.next)
        curr = previous.next
        prev = None
        self.printLinkedList(curr)

        for _ in range(right - left + 1):
            temporary = curr.next

            curr.next = prev
            prev = curr
            curr = temporary

        previous.next.next = curr
        previous.next = prev
        
        return dummy.next
        
    def addOne(self, head):
        rev_head = self.reverseList(head)
        current = rev_head
        carry = 1

        while current:
            current.val = current.val + carry
            if current.val > 9:
                carry = current.val // 10
                current.val = current.val % 10
                print(current.val)
            else:
                break

            if not current.next and carry:
                current.next = ListNode(carry)
                break
            current = current.next
    
        new_head = self.reverseList(rev_head)
        return new_head

    def reverseList(self, head):
        previous = None
        current = head

        while current:
            temporary = current.next
            current.next = previous
            previous = current

            current = temporary

        return previous

    def addTwoNumbers(self,head1,head2):
        curr1 = head1
        curr2 = head2
        
        sumOfTwo = ListNode()
        new_list = sumOfTwo

        carry = 0
        while curr1 or curr2:
            one = curr1.val if curr1 else 0
            two = curr2.val if curr2 else 0

            total = one + two + carry    
            
            carry = total // 10
            new_node = total % 10
            new_list.next = ListNode(new_node)
            new_list = new_list.next
            
            curr1 = curr1.next if curr1 else curr1
            curr2 = curr2.next if curr2 else curr2
        
        if carry != 0:
            new_list.next = ListNode(carry)
        
        return sumOfTwo.next
    
    def oddEvenList(self, head):
        odd = head
        even = head.next
        curr = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next

        odd.next = curr        
        
        return head
    
    def deleteDuplicates(self, head):
        pass
        
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
l1 = s.convertArrayToLL([1,4,3,2,5,2])
# l2 = s.convertArrayToLL([5])
head = s.partition(l1,3)
# head = s.convertArrayToLL( [7,2,4,3])
# sumOfTwo = s.addTwoNumbers(l1,l2)
# new_head = s.oddEvenList(head)
# s.printLinkedList(new_head)
# added = s.addOne(head)
# rl = s.reverseList(head)
# rl = s.reverseBetween(head,2,4)
# swapped = s.swapPairs(head)
# new_head = s.deleteMiddle(head)
s.printLinkedList(head)