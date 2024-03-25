'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def searchInLinkedList(head, k):
    # Your code goes here.
    curr = head
    while curr:
        if curr.data == k:
            return 1
        curr = curr.next
    return 0