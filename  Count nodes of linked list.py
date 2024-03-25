'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    #Your code goes here
    count = 0
    curr = head
    while curr:
        curr = curr.next
        count += 1
    return count