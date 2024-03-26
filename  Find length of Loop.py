class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    # Write your code here
    slow, fast = head, head
    length = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            temp = slow.next
            length += 1
            while slow != temp:
                length += 1
                temp = temp.next
            return length
    return length
    
