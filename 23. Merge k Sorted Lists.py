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
#using Min Heap
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#This solution has a time complexity of O(N log k),
#where N is the total number of nodes across all linked lists and k is the number of linked lists. 
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        
        dummy = ListNode()
        temp = dummy
        heap = []
        
        # Push the first element of each list onto the heap
        for head in lists:
            if head:    
              heapq.heappush(heap, (head.val, id(head), head))
        
        while heap:
            val, _, node = heapq.heappop(heap)
            temp.next = node
            temp = temp.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
        
        return dummy.next

#In Python, the id() function returns the unique identifier (memory address) of an object. 
#It's used here in conjunction with the node's value to ensure that two nodes with the same value don't collide in the heap.

#In other languages like C++ or Java, pointers or references are used to directly represent memory addresses. 
#When comparing pointers or references in these languages, you're essentially comparing memory addresses implicitly.
         