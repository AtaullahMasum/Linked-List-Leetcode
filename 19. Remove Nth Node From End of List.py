#Brute Force Approch
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        position = count - n
        if position == 0:
            return head.next
        temp = head
        while temp:
            position -= 1  
            if position == 0:
                temp.next = temp.next.next
                break
            temp = temp.next
        
        return head
#Optimal Approch
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       dummy = ListNode()
       dummy.next = head
       fast = dummy
       slow = dummy
       for _ in range(n):
          fast = fast.next
       while fast.next:
          slow = slow.next
          fast = fast.next
       slow.next = slow.next.next
       return dummy.next
    