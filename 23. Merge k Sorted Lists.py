# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeSortedList(self, temp1, temp2):
        dummy = ListNode()
        temp = dummy
        t1 = temp1
        t2 = temp2
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head = lists[0]
        for i in range(1, len(lists)):
            head = self.mergeSortedList(head, lists[i])
        return head