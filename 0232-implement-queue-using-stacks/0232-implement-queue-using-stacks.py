class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        return self.q.append(x)

    def pop(self) -> int:
        if self.q:
            return self.q.pop(0)
        else:
            return None

    def peek(self) -> int:
        if self.q:
            return self.q[0]
        else:
            return None

    def empty(self) -> bool:
        if self.q:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()