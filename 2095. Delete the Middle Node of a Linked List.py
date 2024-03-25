# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head 
        fast = head
        prev = None
        # Move slow pointer one step at a time and fast pointer two steps at a time
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Delete the middle node by updating the next pointer of the node before it
        prev.next = slow.next
        return head
        