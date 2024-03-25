class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    # Write your code here
    dumm_head = Node(0)
    for i in range(len(arr)):
        if i== 0:
            dumm_head.next = Node(arr[i])
            curr = dumm_head.next
        else:
            curr.next = Node(arr[i])
            curr = curr.next
    return dumm_head.next