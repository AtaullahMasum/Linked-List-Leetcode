# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        #find lenth and tail node
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        if k%length==0:
            return head
        tail.next = head
        k = k%length
        #find lenth - k node
        temp = head
        count = 1
        while count !=(length-k):
            count += 1
            temp = temp.next
        newhead = temp.next
        temp.next = None
        return newhead