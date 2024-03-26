class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.
def findtail(node):
    temp = node
    while temp.next:
        temp = temp.next
    return temp

def findPairs(head: Node, k: int) -> [[int]]:

    # Write your code here.
    # Return boolean true or false.
    result = []
    left = head
    right = findtail(head)
    while left.data < right.data:
        if left.data + right.data == k:
            result.append([left.data, right.data])
            left = left.next
            right = right.prev
        elif left.data + right.data > k:
            right = right.prev
        else:
            left  = left.next
    return result
