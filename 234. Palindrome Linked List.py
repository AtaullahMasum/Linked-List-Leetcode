# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, prev=None):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverse(next, head)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        newhead = self.reverse(slow.next)
        first = head
        second = newhead
        while second:
            if first.val != second.val:
                self.reverse(newhead)
                return False
            first = first.next
            second = second.next
        self.reverse(newhead)
        return True
        