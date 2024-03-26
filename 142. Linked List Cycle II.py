#using hashset
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return None
        
        hashset = set()
        temp = head
        while temp:
            if temp in hashset:
                return temp
            hashset.add(temp)
            temp = temp.next
        return None