class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left, self.right = [], []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.right.append(x)
        
    def exchange(self):
        while self.right:
            self.left.append(self.right.pop())
        return

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.left:
            self.exchange()
        return self.left.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.left:
            self.exchange()
        return self.left[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.left or self.right:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()