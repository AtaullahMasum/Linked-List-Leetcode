# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, prev =None):
        if not head:
            return prev
        next = head.next
        head.next= prev
        return self.reverse(next, head)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = self.reverse(l1)
        head2 = self.reverse(l2)
        head = ListNode()
        temp = head
        carry = 0
        while head1 or head2 or carry:
            sum =(head1.val if head1 else 0) + (head2.val if head2 else 0) + carry
            carry = sum//10
            sum = sum%10
            temp.next = ListNode(sum)
            temp = temp.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        new_head = self.reverse(head.next)
        return new_head
