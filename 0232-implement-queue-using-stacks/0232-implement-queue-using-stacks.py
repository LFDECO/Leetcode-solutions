class MyQueue:

    def __init__(self):
      self.stack=[]
      self.stack1=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
    def transfer(self):
         while(len(self.stack)):
            self.stack1.append(self.stack[-1])
            self.stack.pop()

    def pop(self) -> int:
        if len(self.stack1)<=0:
            self.transfer()
        return self.stack1.pop()
        

    def peek(self) -> int:
        if len(self.stack1)<=0:
            self.transfer()
        return self.stack1[-1]

    def empty(self) -> bool:
        if len(self.stack1)==0 and len(self.stack)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()