from typing import Node
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    # Write your code here
    temp = head
    while temp:
        if temp.data == k:
            if temp == head:
                head = temp.next
            prevnode = temp.prev
            nextnode = temp.next
            if prevnode:
                prevnode.next = nextnode
            if nextnode:
                nextnode.prev = prevnode
            temp = nextnode
        else:
            temp = temp.next
    return  head