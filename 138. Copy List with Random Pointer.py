"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#Time Complexity is O(2n)
#Space Complexity is O(n) + O(n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        temp = head
        hashmap = {}
        while temp:
            clonenode = Node(temp.val)
            hashmap[temp] = clonenode
            temp = temp.next
        temp = head
        while temp:
            copynode = hashmap[temp]
            copynode.next = hashmap.get(temp.next)
            copynode.random = hashmap.get(temp.random)
            temp = temp.next
        return hashmap[head]
#Optimal Approches
# step 1 insert copy nodes in between two nodes
# step 2 connect Random Pointers
# Step 3 Connect Next Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        #step 1 copy nodes in between two nodes
        temp = head
        while temp:
            copynode = Node(temp.val)
            copynode.next = temp.next
            temp.next = copynode
            temp = temp.next.next
        # step2 connect random pointer
        temp = head
        while temp:
            copynode = temp.next
            if temp.random:
                copynode.random = temp.random.next
            else:
                copynode.random = None
            temp = temp.next.next
        # step 3 connect next pointer
        dummy = Node(-1)
        res = dummy
        temp = head
        while temp:
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next
        return dummy.next
       