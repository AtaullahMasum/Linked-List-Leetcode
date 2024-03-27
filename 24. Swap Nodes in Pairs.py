# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            # Nodes to be swapped
            fast = prev.next
            second = prev.next.next 
            # Swapping
            fast.next = second.next
            second.next = fast
            prev.next = second
            # Move to the next pair
            prev  = fast
          

        return dummy.next
        