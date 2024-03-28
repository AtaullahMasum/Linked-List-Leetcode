# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, lefthead, righthead):
        dummy = ListNode()
        temp = dummy
        t1 = lefthead
        t2 = righthead
        while t1 and t2:
            if t1.val < t2.val:
                temp.next = t1
                t1 = t1.next
            else:
                temp.next = t2
                t2 = t2.next
            temp = temp.next
        if t1:
            temp.next = t1
        else:
            temp.next = t2
        return dummy.next

    def findMiddle(self, head):
        slow = head
        fast = head.next
        #prev = None  # Keep track of the previous node to split the list
        while fast and fast.next:
            #prev = slow  # Update the previous node
            slow = slow.next
            fast = fast.next.next
        #if prev:
        #    prev.next = None  # Split the list at the middle node
        return slow
    def mergeSort(self, head):
        if not head or not head.next:
            return head 
        middleNode = self.findMiddle(head)
        lefthead = head 
        righthead = middleNode.next
        middleNode.next = None
        lefthead = self.mergeSort(lefthead)
        righthead = self.mergeSort(righthead)
        return self.merge(lefthead, righthead)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
