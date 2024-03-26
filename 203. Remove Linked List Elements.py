# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        # Traverse the linked list and remove nodes with the target value
        temp = head
        prev = None
        while temp:
            if temp.val == val:
                if prev:
                    prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next
        
        return head
                