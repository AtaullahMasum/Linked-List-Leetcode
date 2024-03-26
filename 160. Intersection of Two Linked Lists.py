# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        temp1 = headA
        hashset = set()
        while temp1:
            hashset.add(temp1)
            temp1 = temp1.next
        temp2 = headB
        while temp2:
            if temp2 in hashset:
                return temp2
            temp2 = temp2.next
        return None
#Optimal Solution Added
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, node):
        count = 0
        while node:
            count += 1
            node= node.next
        return count
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        temp1 = headA
        temp2 = headB
        length1 = self.length(temp1)
        length2 = self.length(temp2)
        diff = abs(length1 - length2)
        if length1 > length2:
            for _ in range(diff):
                temp1 = temp1.next
        else:
            for _ in range(diff):
                temp2 = temp2.next
        while temp1 and temp2:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None


        
