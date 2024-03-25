# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, prev):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverse(next, head)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
#Iterative solution
class Solution:    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = head
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        return prev

