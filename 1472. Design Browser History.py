class Node:
    def __init__(self, val , back=None, next= None):
        self.val = val
        self.back = back
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.current.next = newNode
        newNode.back = self.current
        self.current = newNode
        

    def back(self, steps: int) -> str:
        while steps:
            if self.current.back:
                self.current = self.current.back
            else:
                break
            steps -= 1
        return self.current.val
    def forward(self, steps: int) -> str:
        while steps:
            if self.current.next:
                self.current = self.current.next
            else:
                break
            steps -= 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)