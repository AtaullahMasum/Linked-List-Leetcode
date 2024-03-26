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
<<<<<<< HEAD
#Optimal Solution Added
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
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
=======
#Optimal Solution Added
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
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
>>>>>>> 7fba3b496a453ac403082fb94246e061286d0e9e