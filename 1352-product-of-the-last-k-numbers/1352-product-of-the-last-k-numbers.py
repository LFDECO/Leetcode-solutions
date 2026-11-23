class ProductOfNumbers:

    def __init__(self):
        # Stores running products; initialized with 1 as a dummy base
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset since any product including this 0 will be 0
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k >= len(self.prefix), a 0 occurred within the last k elements
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]