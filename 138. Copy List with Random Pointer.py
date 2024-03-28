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
        