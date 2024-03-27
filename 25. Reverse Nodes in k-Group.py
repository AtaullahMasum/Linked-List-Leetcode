# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findKthnode(self, temp, k):
       k = k-1
       while temp and k > 0:
            k -= 1
            temp = temp.next
       return temp
    
    def reverse(self, temp, prev= None):
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevnode = None
        while temp:
            # find kth node
            kthnode = self.findKthnode(temp, k)
            # if not find in kthnode
            if not kthnode:
                if prevnode:
                    prevnode.next = temp
                break
            #save nextnode that located kthnode.next
            nextnode = kthnode.next
            #before reversing kthnode sure that kthnode.next = None
            kthnode.next = None
            #reversing first kthnode
            self.reverse(temp)
            #if temp and head located same place than save newhead equal to kthnode
            if temp == head:
                head = kthnode
            else: # else prevnode.next = kthnode
                prevnode.next = kthnode
            prevnode = temp
            temp = nextnode
        return head