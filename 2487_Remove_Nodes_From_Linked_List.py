class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list():
    head = ListNode(5)
    head.next = ListNode(2)
    head.next.next = ListNode(13)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(8)
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def removeNodes(head):
    #     stack = []
    # current = head
    
    # while current:
    #     stack.append(current.val)
    #     current = current.next
    
    # current = stack.pop()
    # maximum = current
    # result_head = ListNode(current)

    # while stack:
    #     current = stack.pop()
    #     if current < maximum:
    #         continue
    #     else:
    #         new_list = ListNode(current)
    #         new_list.next = result_head
    #         result_head = new_list
    #         maximum = current
    # return result_head
    # node_values = []

    # while head:
    #     node_values.append(head.val)
    #     head = head.next
    
    # stack = []
    # for node in node_values:
    #     while stack and stack[-1] < node:
    #         stack.pop()
    #     stack.append(node)

    # dummy = ListNode(0)
    # current = dummy

    # for value in stack:
    #     current.next = ListNode(value)
    #     current = current.next
    
    # return dummy.next

result = create_linked_list()
new_list = removeNodes(result)
print_linked_list(new_list)