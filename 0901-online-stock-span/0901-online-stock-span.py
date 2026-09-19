class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        if len(self.stack)==0:
            self.stack.append((price,1))
        else:
            span=1
            while self.stack and self.stack[-1][0]<=price :
                ele,spa=self.stack.pop()
                span+=spa
            else:
                self.stack.append((price,span))

        return self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)