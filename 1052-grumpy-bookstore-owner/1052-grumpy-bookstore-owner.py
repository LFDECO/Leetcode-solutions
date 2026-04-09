class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        window_size=minutes
        sum1=0
        for i in range(window_size):
            if grumpy[i]==1:
                sum1+=customers[i]
        result=sum1
        result1=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                result1+=customers[i]
        for i in range(window_size,len(customers)):
            if grumpy[i]==1:
                sum1+=customers[i]
            if grumpy[i-window_size]==1:
                sum1-=customers[i-window_size]
            result=max(sum1,result)
        result+=result1
        return result
