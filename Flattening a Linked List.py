'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
def merge(temp1, temp2):
    dummy = Node(-1)
    temp = dummy
    t1 = temp1
    t2 = temp2
    while t1 and t2:
        if t1.data < t2.data:
            temp.bottom = t1
            t1 = t1.bottom
        else:
            temp.bottom = t2
            t2 = t2.bottom
        temp = temp.bottom
    if t1:
        temp.bottom = t1
    else:
        temp.bottom = t2
    return dummy.bottom
def convert(root):
    if not root or not root.next:
        return root
    mergehead = convert(root.next)
    return merge(root, mergehead)

def flatten(root):
    #Your code here
    return convert(root)
