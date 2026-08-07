class MinStack:

    def __init__(self):
        self.stack=[]
        self.minst=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minst)>0:
            if self.stack[-1]<self.minst[-1]:
                self.minst.append(self.stack[-1])
            else:
                self.minst.append(self.minst[-1])
        else:
            self.minst.append(self.stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minst.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()